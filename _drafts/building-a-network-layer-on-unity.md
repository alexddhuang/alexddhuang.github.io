---
title: "Building a Network Layer on Unity"
categories: IT
tags: game-dev unity csharp network
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