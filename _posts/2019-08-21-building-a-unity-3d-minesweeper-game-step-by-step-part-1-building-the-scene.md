---
title: "Building a Unity 3D Minesweeper Game Step by Step Part 1: Building the Scene"
date: 2019-08-21 17:53:49 +0800
categories: IT
tags: csharp game-development unity
---

In this tutorial, we are going to try to build a 3D [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game in Unity. This is part 1.

Minesweeper is a classical single-player puzzle game. The objective of the game is to clear all hidden "mines" in a board without detonating them. There are many variations of this game exist on many platforms. Most of them are 2D games. However, in this tutorial, we are going to make a 3D version.

In our scene, there is a character standing in a plane, which is built on multiple bricks. When the user touches a brick, the character will move to there. When the character steps on a brick, if there is a mine under the brick, the character stops walking and the health value decreases by one, otherwise the number of mines around the brick is displayed above the brick.

First, create a new 3D project named "Minesweeper3D".

## Preparing the Brick Prefab

Create a Cube object in the sample scene, name it `Brick` and make it to a Prefab.

Next, we need to draw a texture on the surface of `Brick`. Download below two files and import them into the `Textures` folder:

- [`MinesweeperSpritesheet.png`](https://github.com/alexddhuang/Minesweeper3D/blob/part1/Assets/Textures/MinesweeperSpritesheet.png)
- [`MinesweeperSpritesheet.png.meta`](https://github.com/alexddhuang/Minesweeper3D/blob/part1/Assets/Textures/MinesweeperSpritesheet.png.meta)

Please don't forget to download and import `MinesweeperSpritesheet.png.meta` except that you want to manually slice sprites from this sprites sheet by yourself.

Drag the `TileUnknown` sprite onto the `Brick` object. Set the rotation of this sprite as `(90, 0, 90)`, and adjust the position along the `Y` axis as `0.51` so that let this sprite is a little above `Brick`. Adjust the scale of this sprite so thaht let it covers `Brick` just look like this:

{% include image.html name="brick.png" %}

## Building the Scene

You can download the [sample scene](https://github.com/alexddhuang/Minesweeper3D/blob/part1/Assets/Scenes/SampleScene.unity) I made or build it by yourself. You can first make a grid of 20x20 bricks in the scene, and then delete some bricks and insert plain Cubes into those holes. These plain Cubes plays the role of obstacles.

{% include image.html name="scene-part-1.png" %}

Now, our first part of this tutorial is done, let's take a rest and drink a cup of coffee.
