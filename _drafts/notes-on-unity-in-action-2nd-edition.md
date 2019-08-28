---
title: "Notes on \"Unity in Action, 2nd Edition\""
categories: IT
tags: unity game-dev csharp
toc: true
---

[*Unity in Action: Multiplatform game development in C#*, 2nd Edition](https://www.manning.com/books/unity-in-action-second-edition) (2018) by [Joseph Hocking](http://www.newarteest.com/). I have created a [playground](https://github.com/alexddhuang/uia2e-playground) for this book.

## Part 1. First steps

### Chapter 1. Getting to know Unity

#### Why is Unity so great?

- An extremely productive visual workflow
- A high degree of cross-platform support
- The modular component system used to construct game objects.

### Chapter 2. Building a demo that puts you in 3D space

#### Script component for looking around: `MouseLook`

- Horizontal rotation

    ```c#
    transform.Rotate(0, Input.GetAxis("Mouse X") * sensitivityHor, 0);
    ```

    The [`Rotate`](https://docs.unity3d.com/ScriptReference/Transform.Rotate.html) method applies a rotation of Euler angles, first around the z-axis, then x-axis and then y-axis.

    [`Input.GetAxis`](https://docs.unity3d.com/ScriptReference/Input.GetAxis.html) returns the value of the virtual axis identified by an axis name. The value is in the range of `[-1, 1]`.

- Vertical rotation with limits

    ```c#
    _rotationX -= Input.GetAxis("Mouse Y") * sensitivityVert;
    _rotationX = Mathf.Clamp(_rotationX, minimumVert, maximumVert);
    transform.localEulerAngles = new Vector3(_rotationX, transform.localEulerAngles.y, 0);;
    ```

    Because the vertical rotation has limits, we can't directly call `Rotate`. Instead, we need a private variable to hold the current vertical rotation, if it is out of the range, we clamp it into the range by calling [`Mathf.Clamp`](https://docs.unity3d.com/ScriptReference/Mathf.Clamp.html). The statement of setting a new local Euler angle looks a little bit complicated, you may want to write 
    
    ```c#
    transform.localEulerAngles.x = _rotationX;
    ``` 
    
    but [`transform.localEulerAngles`](https://docs.unity3d.com/ScriptReference/Transform-localEulerAngles.html) is in fact a function which returns a temporary vector, so this is invalid and you have to set a new vector to `transform.localEulerAngles`.

- Horizontal and vertical rotation at the same time

    ```c#
    _rotationX -= Input.GetAxis("Mouse Y") * sensitivityVert;
    _rotationX = Mathf.Clamp(_rotationX, minimumVert, maximumVert);
    float rotationY = transform.localEulerAngles.y + Input.GetAxis("Mouse X") * sensitivityHor;
    transform.localEulerAngles = new Vector3(_rotationX, rotationY, 0);
    ```
