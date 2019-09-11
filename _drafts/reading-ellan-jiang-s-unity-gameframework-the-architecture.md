---
title: "Reading Ellan Jiang's Unity GameFramework: The Architecture"
categories: IT
tags: unity game-dev csharp
---

[Ellan Jiang](https://github.com/EllanJiang)'s [Unity GameFramework](https://github.com/EllanJiang/GameFramework) is a popular (1400+ stars on GitHub on September 2019) and elegant framework for Unity game programmer. I want to walk through the codebase and take some notes on it. I think this is a good way to learn it.

There are many modules supported by the GameFramework, including `DownloadManager`, `EntityManager`, `EventManager`, and `FsmManager` etc. Each class of these modules has to implement an abstract class `GameFrameworkModule`, which looks like

```c#
internal abstract class GameFrameworkModule
{
    internal virtual int Priority
    {
        get
        {
            return 0;
        }
    }

    internal abstract void Update(float elapseSeconds, float realElapseSeconds);

    internal abstract void Shutdown();
}
```

The `Update` method is like the [`MonoBehaviour.Update`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) method, that is used to update some states of objects. For that the framework works correctly, you (the user) have to call, in a specific place, the `Update` method of every module. The GameFramework also provides a static class `GameFrameworkEntry` which lets you can easily do this job.

For example, you can create a script called `Entry`, which [shouldn't be destroyed](https://docs.unity3d.com/ScriptReference/Object.DontDestroyOnLoad.html) after the game is launched. In `Entry.Update`, you can write `GameFrameworkEntry.Update(Time.deltaTime, Time.deltaTime);` to update every module. Here is its implementation:

```c#
public static void Update(float elapseSeconds, float realElapseSeconds)
{
    foreach (GameFrameworkModule module in s_GameFrameworkModules)
    {
        module.Update(elapseSeconds, realElapseSeconds);
    }
}
```

The `Priority` method is used for deciding the priority of updating of each module.

The `Shutdown` method expects to be invoked when the game shuts down. Similarly, `GameFrameworkEntry` 