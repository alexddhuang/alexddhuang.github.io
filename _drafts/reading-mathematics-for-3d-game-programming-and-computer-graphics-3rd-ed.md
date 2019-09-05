---
title: "Reading Mathematics for 3D Game Programming and Computer Graphics, 3rd ED"
categories: IT
tags: math computer-graphics game-dev
toc: true
---

[*Mathematics for 3D Game Programming and Computer Graphics*, 3rd Edition](http://canvas.projekti.info/ebooks/Mathematics%20for%203D%20Game%20Programming%20and%20Computer%20Graphics,%20Third%20Edition.pdf) (2011) by [Eric Lengyel](https://twitter.com/ericlengyel).

## Chapter 1. The Rendering Pipeline

### 1.1 Graphics Processors

> Most importantly, VRAM (Video Random Access Memory) contains the front and back image buffers. The front image buffer contains the exact pixel data that is visible in the viewport. The viewport is the area of the display containing the rendered image and may be a subregion of a window, the entire contents of a window, or the full area of the display. The back image buffer is the location to which the GPU actually renders a scene. The back buffer is not visible and exists so that a scene can be rendered in its entirety before being shown to the user. Once an image has been completely rendered, the front and back image buffers are exchanged. This operation is called a buffer swap and can be performed either by changing the memory address that represents the base of the visible image buffer or by copying the contents of the back image buffer to the front image buffer. The buffer swap is often synchronized with the refresh frequency of the display to avoid an artifact known as tearing. Tearing occurs when a buffer swap is performed during the display refresh interval, causing the upper and lower parts of a viewport to show data from different image buffers.

The buffer swap must wait for the finish of writing data to the back buffer to execute. For avoiding the pending of GPU, I think maybe the image buffers can be replaced by an image buffers queue.
