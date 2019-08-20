---
title: "Building a Unity 3D Minesweeper Game Step by Step Part 1: Building the Scene"
categories: IT
tags: csharp game-development unity
---

In this tutorial, we are going to try to build a 3D [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game in Unity. This is part 1.

Minesweeper is a classical single-player puzzle game. The objective of the game is to clear all hidden "mines" in a board without detonating them. There are many variations of this game exist on many platforms. Most of them are 2D games. However, in this tutorial, we are going to make a 3D version.

In our scene, there is a character standing in a plane, which is built on multiple bricks. When the user touches a brick, the character will move to there. When the character steps on a brick, if there is a mine under the brick, the character stops walking and the health value decreases by one, otherwise the number of mines around the brick is displayed above the brick.

First, create a new 3D project named "Minesweeper3D".

## Preparing the Brick Prefabs

Create a Cube object in the sample scene, name it `Brick` and make it to a Prefab.
