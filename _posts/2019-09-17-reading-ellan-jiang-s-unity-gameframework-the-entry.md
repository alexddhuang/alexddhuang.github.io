---
title: "Reading Ellan Jiang's Unity GameFramework: The Entry"
date: 2019-09-17 20:28:22 +0800
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

For example, you can create a script called `Entry`, which [shouldn't be destroyed](https://docs.unity3d.com/ScriptReference/Object.DontDestroyOnLoad.html) after the game is launched. In `Entry.Update`, you can write the below statement to update every module. 

```c#
GameFrameworkEntry.Update(Time.deltaTime, Time.deltaTime);
```

Here is the implementation of it:

```c#
public static void Update(float elapseSeconds, float realElapseSeconds)
{
    foreach (GameFrameworkModule module in s_GameFrameworkModules)
    {
        module.Update(elapseSeconds, realElapseSeconds);
    }
}
```

The `Shutdown` method expects to be invoked when the game shuts down. Similarly, `GameFrameworkEntry` provides a method to shut down all modules:

```c#
public static void Shutdown()
{
    for (LinkedListNode<GameFrameworkModule> current = s_GameFrameworkModules.Last; current != null; current = current.Previous)
    {
        current.Value.Shutdown();
    }

    s_GameFrameworkModules.Clear();
    ReferencePool.ClearAll();
    GameFrameworkLog.SetLogHelper(null);
}
```

The `Priority` method is used for deciding the priority of updating of each module. `s_GameFrameworkModules` is a linked list to hold all game modules. The `Priority` larger, the position of the relative game module at `s_GameFrameworkModules` is fronter.

How to get each module? You just need to call `GameFrameworkEntry.GetModule<T>()`; If the game module you request is not existed, it will create one.

```c#
private static GameFrameworkModule CreateModule(Type moduleType)
{
    GameFrameworkModule module = (GameFrameworkModule)Activator.CreateInstance(moduleType);
    if (module == null)
    {
        throw new GameFrameworkException(Utility.Text.Format("Can not create module '{0}'.", moduleType.FullName));
    }

    LinkedListNode<GameFrameworkModule> current = s_GameFrameworkModules.First;
    while (current != null)
    {
        if (module.Priority > current.Value.Priority)
        {
            break;
        }

        current = current.Next;
    }

    if (current != null)
    {
        s_GameFrameworkModules.AddBefore(current, module);
    }
    else
    {
        s_GameFrameworkModules.AddLast(module);
    }

    return module;
}
```