---
title: "Reading Reading Ellan Jiang's Unity GameFramework: The NetworkManager"
categories: IT
tags: unity game-dev csharp
---

[Ellan Jiang](https://github.com/EllanJiang)'s [Unity GameFramework](https://github.com/EllanJiang/GameFramework) is a popular (1400+ stars on GitHub on September 2019) and elegant framework for Unity game programmer. I want to walk through the codebase and take some notes on it. I think this is a good way to learn it.

## How to Get the NetworkManager?

```c#
var networkManager = GameFrameworkEntry.GetModule<INetworkManager>();
```

## How to Initialize a Network Channel?

`NetworkManager` supports multiple network channels. Normally, you just need only one network channel in your game. The initialization of a network channel includes three steps: 1. Creating a network channel; 2. Connecting to a game server; 3. Setting listeners for network events.

```c#
var channel = networkManager.CreateNetworkChannel("GameServer", GameServerNetworkChannelHelper.Instance);
channel.Connect(IPAddress.Parse(ip), port);

networkManager.NetworkConnected     += OnNetworkConnected;
networkManager.NetworkClosed        += OnNetworkClosed;
networkManager.NetworkMissHeartBeat += OnNetworkMissHeartBeat;
networkManager.NetworkError         += OnNetworkError;
```

The `CreateNetworkChannel` method accepts a channel name and an instance of `INetworkChannelHelper`. You have to implement an `INetworkChannelHelper` in your game for each network channel. In the example above, the implemented class is called `GameServerNetworkChannelHelper`.
