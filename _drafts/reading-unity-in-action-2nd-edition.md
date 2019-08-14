---
title: "Reading Unity in Action, 2nd Edition"
category: IT
tags: unity game-development c#
toc: true
---

[Joseph Hocking](http://www.newarteest.com/)'s [*Unity in Action*, 2nd Edition](https://www.manning.com/books/unity-in-action-second-edition) was published in 2018. I choose it as my first book for learning [Unity](https://unity.com/). All of the sample projects from the book can be found on [GitHub](https://github.com/jhocking/uia-2e). I have forked that repo and created a [`playground`](https://github.com/alexddhuang/uia-2e/tree/playground) branch so that I can safely build these projects step-by-step.

## Part 1. First steps

### Chapter 1. Getting to know Unity

#### What make Unity so great?

> Unity has two main advantages over similar cutting-edge game development tools: **an extremely productive visual workflow** and **a high degree of cross-platform support**.

> A third, more subtle, benefit comes from the **modular component system** used to construct game objects.

A component system is more flexible than a class hierarchy.

#### Operating the Unity editor

More information can be found on the [official docs](https://docs.unity3d.com/Manual/UnityOverview.html).

#### Programming in Unity

All code execution in Unity starts from scripts linked to an object in the scene. Only those scripts inherited from `MonoBehaviour` can be components. You can overrides some methods of `MonoBehaviour` to do game logic. These methods include

- `Start()`, called once when the object becomes active (which is generally as soon as the level with that object has loaded).
- `Update()`, called every frame.

#### Comparing C# and JavaScript

C# is strongly typed, whereas JavaScript is not. [JavaScript was removed from Unity](https://blogs.unity3d.com/2017/08/11/unityscripts-long-ride-off-into-the-sunset/).

### Chapter 2. Building a demo that puts you in 3D space

#### Understanding 3D coordinate space 

Unity uses left-handed 3D dimensional Descartes coordinates

#### Putting a player in a scene

We use a Capsule game object to represent the player in this chapter. The Capsule object has a default [Capsule Collider](https://docs.unity3d.com/Manual/class-CapsuleCollider.html) component, we need to replace it with the [Character Controller](https://docs.unity3d.com/Manual/class-CharacterController.html) componenet. Why? 

> The traditional Doom-style first person controls are not physically realistic. The character runs 90 miles per hour, comes to a halt immediately and turns on a dime. Because it is so unrealistic, use of Rigidbodies and physics to create this behavior is impractical and will feel wrong. The solution is the specialized Character Controller. It is simply a capsule shaped Collider which can be told to move in some direction from a script. The Controller will then carry out the movement but be constrained by collisions. It will slide along walls, walk up stairs (if they are lower than the Step Offset) and walk on slopes within the Slope Limit.
> 
> -- [Character Controller \| Unity Docs](https://docs.unity3d.com/Manual/class-CharacterController.html)

#### Writing a script that moves objects

The first script is called `MouseLook`, which handles mouse inputs to rotate the player object.

Code framewrok:

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MouseLook : MonoBehaviour
{
    public enum RotationAxes {
        MouseXAndY = 0,
        MouseX = 1,
        MouseY = 2
    }

    public RotationAxes axes = RotationAxes.MouseXAndY;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (axes == RotationAxes.MouseX) {
            // horizontal rotation here
        } else if (axes == RotationAxes.MouseY) { 
            // vertical rotation here
        } else {
            // both horizontal and vertical rotation here
        }
    }
}
```

Handling the horizontal rotation is simple, just invoking the [`Transform.Rotate`](https://docs.unity3d.com/ScriptReference/Transform.Rotate.html) method:

```c#
transform.Rotate(0, Input.GetAxis("Mouse X") * sensitivityHor, 0);
```

`Input.GetAxis` returns the value (in the range -1 .. 1) of the virtual axis. `Transform.Rotate` applies a roation in the order of z -> x -> y.

Handling the vertical rotation is a little bit complicated:

```c#
_rotationX -= Input.GetAxis("Mouse Y") * sensitivityVert;
_rotationX = Mathf.Clamp(_rotationX, minimumVert, maximumVert);

float rotationY = transform.localEulerAngles.y;

transform.localEulerAngles = new Vector3(_rotationX, rotationY, 0);
```

Because the vertical rotation angle has limits, we need a variable `_rotationX` to record its rotated angle, if it escapes the range, we need to clamp it. That is what done by the first two lines. The next two lines look not very natural, why don't just

```c#
transform.localEulerAngles.x = _rotationX;
```

Well, because in fact, `transform.localEulerAngles` is not a property, it is a method, so it returns a temporary vector, which you can't assign a value to it.

Handling horizontal and vertical rotation at the same time is a combination of above code:

```c#
_rotationX -= Input.GetAxis("Mouse Y") * sensitivityVert;
_rotationX = Mathf.Clamp(_rotationX, minimumVert, maximumVert);

float rotationY = transform.localEulerAngles.y + Input.GetAxis("Mouse X") * sensitivityHor;

transform.localEulerAngles = new Vector3(_rotationX, rotationY, 0);
```


#### Implementing FPS controls
