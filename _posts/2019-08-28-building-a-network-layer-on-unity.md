---
title: "Building a Network Layer on Unity"
date: 2019-08-28 11:30:30 +0800
categories: IT
tags: game-dev unity csharp network
toc: true
---

Here is a note on how to build a network layer on [Unity](https://unity.com/). I am going to create a `TCPClient` class, which is a simple wrapper of [`System.Net.Sockets.TcpClient`](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.tcpclient).

## Interfaces

```c#
public interface IDataParser
{
    void Parse(byte[] bytes);
}

public class TCPClient : MonoBehaviour
{
    public string IP = "127.0.0.1";
    public int PORT = 0;

    public void Send(byte[] bytes) 
    {

    }

    public void Listen(IDataParser parser) 
    {

    }
}
```

The `TCPClient` class is very simple -- Two main things it just does: sending data and listening to data. How data is serialized and deserialized, depending on the game, so the `Listen` method just receives an abstract data parser. It's the user's job to implement a concrete data parser.

## Implementations

### Reading Data

```c#
void Start()
{
    try {
        _client = new TcpClient(IP, PORT);
    } catch (SocketException e) {
        Debug.Log($"Socket exception: {e}");
    }

    if (_client != null && _client.Connected) {
        try {
            _receivingDataThread = new Thread(new ThreadStart(ReceivingData));
            _receivingDataThread.IsBackground = true;
            _receivingDataThread.Start();
        } catch (Exception e) {
            Debug.Log($"Exception: {e}");
        }
    }
}
```

In the `TCPClient.Start` method, we create a new instance of `TcpClient`, then we start a new thread for receiving data. We are going to send and receive data on an instance of [`NetworkStream`](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream), that class provides methods for sending and receiving data over `Stream` sockets in **blocking mode**. We can also use its asynchronous methods, but for simple coding, let us temporarily work on the blocking mode.

> Read and write operations can be performed simultaneously on an instance of the `NetworkStream` class without the need for synchronization. As long as there is one unique thread for the write operations and one unique thread for the read operations, there will be no cross-interference between read and write threads and no synchronization is required.
> 
> -- [Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream)

That's why we need to create a new thread to receive data.

```c#
private void ReceivingData() 
{
    var stream = _client.GetStream();
    while (_client.Connected) {
        if (stream.CanRead && _client.Available > 0) {
            var header = new byte[2];
            var num = stream.Read(header, 0, header.Length);
            if (num > 0) {
                short size = BitConverter.ToInt16(header, 0);
                size = IPAddress.NetworkToHostOrder(size);

                var buffer = new byte[size - header.Length];
                var offset = 0;
                var remain = buffer.Length;
                do {
                    offset += stream.Read(buffer, offset, remain);
                    remain = buffer.Length - offset;
                } while (offset < buffer.Length);

                if (_parser != null) {
                    _parser.Parse(buffer);
                }
            }
        }
    }

    _receivingDataThread.Abort();
}
```

Here we assume that the length of the header is 2 bytes, i.e. the data type of header is `short`; The header indicates the length of a packet.

Now we can implement the `Listen` method:

```c#
public void Listen(IDataParser parser) 
{
    _parser = parser;
}
```

### Sending Data

The implementation of `Send` is just the reverse process of reading data: We need to insert a header into the buffer.

```c#
public void Send(byte[] bytes) 
{
    if (_client != null && _client.Connected) {
        var stream = _client.GetStream();
        if (stream.CanWrite) {
            short size = (short) (bytes.Length + 2);
            byte[] header = BitConverter.GetBytes(IPAddress.HostToNetworkOrder(size));
            byte[] packet = new byte[header.Length + bytes.Length];
            header.CopyTo(packet, 0);
            bytes.CopyTo(packet, header.Length);

            stream.Write(packet, 0, packet.Length);
        }
    }
}
```

### The Data Parser

Here we implement a data parser named `MessageCenter`. This class uses [Google's Protocol Buffers](https://developers.google.com/protocol-buffers/). 

```c#
public class MessageCenter : MonoBehaviour, IDataParser
{
    public TCPClient client;

    public void Parse(byte[] bytes) 
    {
        
    }

    void Start()
    {
        client.Listen(this);
    }
}
```

We use a `short` data type to represent each command in the game. Each data packet contains a head and a body, the head is a command enumeration, and the body is a serialization of the message structure. The developer needs to create an individual class to handle each command, and each class needs to implement `IMessageHandler`.

```c#
public interface IMessageHandler
{
    void Handle(short cmd, byte[] buffer);
}
```

`MessageCenter` should provide a method to register each handler:

```c#
private Dictionary<short, IMessageHandler> _handlers = new Dictionary<short, IMessageHandler>();

public void Register(short cmd, IMessageHandler handler)
{
    _handlers.Add(cmd, handler);
}
```

Now we can implement the `Parse` method:

```c#
public void Parse(byte[] bytes) 
{
    byte[] head = new byte[2];
    Buffer.BlockCopy(bytes, 0, head, 0, 2);
    
    short cmd = BitConverter.ToInt16(head, 0);
    cmd = IPAddress.NetworkToHostOrder(cmd);

    byte[] body = new byte[bytes.Length - 2];
    Buffer.BlockCopy(bytes, 2, body, 0, bytes.Length - 2);

    IMessageHandler handler;
    var ok = _handlers.TryGetValue(cmd, out handler);
    if (ok) {
        handler.Handle(cmd, body);
    }
}
```

Next, we write a `Send` method for `MessageCenter` so that the user can conveniently send messages.

```c#
using pb = global::Google.Protobuf;

// ...

public void Send(short cmd, pb.IMessage message)
{
    byte[] head = BitConverter.GetBytes(IPAddress.HostToNetworkOrder(cmd));
    int bodySize = message.CalculateSize();
    byte[] body = new byte[bodySize];
    
    pb.CodedOutputStream output = new pb.CodedOutputStream(body);
    message.WriteTo(output);

    byte[] buffer = new byte[head.Length + body.Length];
    head.CopyTo(buffer, 0);
    body.CopyTo(buffer, head.Length);

    client.Send(buffer);
}
```

The network layer is finished at this moment, but let us write an example to test it.

## An Example

Suppose we have a login command `100`, whose message structure is

```
package playermgr;

message LoginReq {
    string username=1;
    string password=2;
}

message LoginRsp {
    enum Result {
        SUCCESS=0;
        USERNAME_PW_ERROR=1;
        LOGIN_OTHER=2;
    }
    Result  result=1;
    int32   userid=2;
    string  username=3;
    int32   glod=4;
}
```

Now we create a script `LoginHandler`:

```c#
using UnityEngine;

using AXUnityFramework.Network;
using pb = global::Google.Protobuf;

public class LoginHandler : MonoBehaviour, IMessageHandler 
{
    public MessageCenter messageCenter;
    public TCPClient client;

    private bool _testMessageSent = false;

    public void Handle(short cmd, byte[] buffer)
    {        
        Playermgr.LoginRsp message = new Playermgr.LoginRsp();

        pb.CodedInputStream input = new pb.CodedInputStream(buffer);
        message.MergeFrom(input);

        Debug.Log($"Handle {cmd}");
        Debug.Log($"result: {message.Result}");
        Debug.Log($"username: {message.Username}");
        Debug.Log($"userid: {message.Userid}");
        Debug.Log($"glod: {message.Glod}");
    }

    void Start()
    {
        messageCenter.Register(100, new LoginHandler());
    }

    void Update()
    {
        if (client.IsConnected() && !_testMessageSent) {
            SendTestMessage();
        }
    }

    private void SendTestMessage() 
    {
        Playermgr.LoginReq req = new Playermgr.LoginReq();
        req.Username = "test1";
        req.Password = "123456";

        messageCenter.Send(100, req);

        _testMessageSent = true;
    }
}
```