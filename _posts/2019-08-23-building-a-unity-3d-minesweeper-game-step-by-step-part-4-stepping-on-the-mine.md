---
title: "Building a Unity 3D Minesweeper Game Step by Step Part 4: Stepping on the Mine"
date: 2019-08-23 11:17:43 +0800
categories: IT
tags: csharp game-dev unity
---

In this tutorial, we are going to try to build a 3D [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game in Unity. This is part 4. The complete project is [here](https://github.com/alexddhuang/Minesweeper3D).

At the end of [part 3](/2019/08/22/building-a-unity-3d-minesweeper-game-step-by-step-part-3-burying-mines.html) of this tutorial, we have almost done our game. We can see that when the character runs over a mine, it didn't get hurt and continue to move. This part provides a tiny improvement of this defect. 

We don't hope to immediately kill the character when it steps on a mine. Instead, we give it a warning. When the character receives this warning, it will step back one brick, and its blood decreases one. For accomplishing this purpose, we need to keep a track of bricks it walks through.

First, add these two fields to the class `CharacterController`.

```c#
public int blood = 5;
private Brick mPreviousBrick;
private Brick mCurrentBrick;
```

Then modify the `DetectMine` method as below.

```c#
private void DetectMine()
{
    Ray ray = new Ray(transform.position, -transform.up);
    RaycastHit hit;
    if (Physics.SphereCast(ray, 0.2f, out hit)) {
        GameObject hitObject = hit.transform.gameObject;
        Brick brick = hitObject.GetComponent<Brick>();
        if (brick != null) {
            brick.ShowSecret();

            if (brick.mine && mPreviousBrick != null) {
                mMeshAgent.SetDestination(mPreviousBrick.transform.position);
                blood -= 1;
            }

            if (brick != mCurrentBrick) {
                mPreviousBrick = mCurrentBrick;
                mCurrentBrick = brick;
            }
        }
    }
}
```

It is very easy to understand. If the character steps on a mine and the previous brick is not null, we just set the position of the previous brick as the new destination for the mesh agent, and then decrease the blood with 1.

{% include image.html name="bomb.gif" %}

Now, our tutorial is all done, but of course, you can freely continue to improve this game. I'm going to drink coffee, goodbye.

## Further Reading

- [Part 1: Building the Scene](/2019/08/21/building-a-unity-3d-minesweeper-game-step-by-step-part-1-building-the-scene.html)
- [Part 2: The Character](/2019/08/22/building-a-unity-3d-minesweeper-game-step-by-step-part-2-the-character.html)
- [Part 3: Burying Mines](/2019/08/22/building-a-unity-3d-minesweeper-game-step-by-step-part-3-burying-mines.html)
