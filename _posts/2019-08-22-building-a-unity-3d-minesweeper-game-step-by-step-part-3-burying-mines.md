---
title: "Building a Unity 3D Minesweeper Game Step by Step Part 3: Burying Mines"
date: 2019-08-22 17:51:32 +0800
date_modified: 2019-08-22 20:29:04 +0800
categories: IT
tags: csharp game-dev unity
---

In this tutorial, we are going to try to build a 3D [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game in Unity. This is part 3.

Modify the `Brick` script as below.

```c#
public class Brick : MonoBehaviour
{
    public bool mine = false;

    public float radius = 1.42f;

    private List<Brick> mNeighbors;

    // Start is called before the first frame update
    void Start()
    {
        FindNeighbors();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void FindNeighbors()
    {
        var allBricks = GameObject.FindGameObjectsWithTag("Brick");

        mNeighbors = new List<Brick>();

        for (int i = 0; i < allBricks.Length; i++) {
            var brick = allBricks[i];
            var distance = Vector3.Distance(transform.position, brick.transform.position);
            if (0 < distance && distance <= radius) {
                mNeighbors.Add(brick.GetComponent<Brick>());
            }
        }
    }
}
```

It has two public fields. `mine` indicates whether `Brick` has a mine. `radius` is used to detect whether another `Brick` is its neighbor, and the default value is `1.42f`.

Now you can select some `Brick`s in the scene to tick the Mine checkbox of them.

NOTE: For improving the runtime performance, you can also make `mNeighbors` to be public, and invoke `FindNeighbors` in the [`OnValidate`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnValidate.html) method instead of in `Start` so that this work is given to the editor.

Next, we write a method to show the secret of a `Brick`: If it has a mine, showing a bomb, else showing the number of mines in its neighbors. Before that, we need to build a sprites map. Add the following line inside the `Brick` class:

```c#
private static Dictionary<string, Sprite> mTileImages;
```

Then write a method `BuildSpritesMap` and invoke it in the `Start` (Make sure that `MinesweeperSpritesheet.png` is placed in the folder `Resources/Sprites`).

```c#
public static void BuildSpritesMap()
{
    if (mTileImages == null) {
        Sprite[] sprites = Resources.LoadAll<Sprite>("Sprites/MinesweeperSpritesheet");
        mTileImages = new Dictionary<string, Sprite>();
        for (int i = 0; i < sprites.Length; i++) {
            mTileImages.Add(sprites[i].name, (Sprite) sprites[i]);
        }
    }
}
```

Now, we can write our `ShowSecret` method:

```c#
public void ShowSecret()
{
    if (mShowed) return;

    mShowed = true;

    string name;

    if (mine) {
        name = "TileMine";
    } else {
        int num = 0;
        mNeighbors.ForEach(brick => {
            if (brick.mine) num += 1;
        });
        name = $"Tile{num}";
    }

    Sprite sprite;
    if (mTileImages.TryGetValue(name, out sprite))
        tile.sprite = sprite;
}
```

`tile` is a public field of type `SpriteRenderer`. Don't forget to bind it to the tile sprite renderer which we already have set up to the `Brick` prefab in [part 1](/2019/08/21/building-a-unity-3d-minesweeper-game-step-by-step-part-1-building-the-scene.html) of this tutorial.

When to show the secret of a brick? At the time the character steps on the brick. How to detect this event? Again, we are going to summon the magic of [Raycasting](https://en.wikipedia.org/wiki/Ray_casting). We cast a ray from the character along the downward direction. When this ray hit a brick, we invoke its `ShowSecret` method.

Add the method below to the `CharacterController` class and invoke it in the `Update` method:

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
        }
    }
}
```

Now our game is almost done. You can play it.

{% include image.html name="show-secret.gif" %}

## Further Reading

- [Part 1: Building the Scene](/2019/08/21/building-a-unity-3d-minesweeper-game-step-by-step-part-1-building-the-scene.html)
- [Part 2: The Character](/2019/08/22/building-a-unity-3d-minesweeper-game-step-by-step-part-2-the-character.html)
