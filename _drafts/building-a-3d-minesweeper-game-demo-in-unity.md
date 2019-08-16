---
title: "Building a 3D Minesweeper Game Demo in Unity"
categories: IT
tags: game-development unity csharp
---

Recently, I am building a 3D Minesweeper game demo in Unity. Here is a record of the building steps.

## Building the Scene

The scene in this demo was very simple, just a 100x100 grid of mine points. I used a Cube to represent a mine point, and I didn't want to manually build this scene, so I created a script named `Architect` which will automatically generate these mine points.

```c#
public class Architect : MonoBehaviour
{
    [SerializeField]
    private GameObject minePointPrefab;

    [SerializeField]
    private GameObject minePointsHolder;

    // Start is called before the first frame update
    void Start()
    {
        GenerateMinePoints();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void GenerateMinePoints() 
    {
        for (int i = 0; i < 100; i++)
            for (int j = 0; j < 100; j++) {
                GameObject point = Instantiate(minePointPrefab) as GameObject;
                point.transform.position = new Vector3(i - 49.5f, 1, 49.5f - j);
                point.transform.SetParent(minePointsHolder.transform);
            }
    }
}
```

## Controlling the Player Moving

I used a Capsule to represent the player, and added a Character Controller component to it. Next, I created a script named `PlayerInput` to handle the user input. I hoped when the user clicks the screen, the player will move to a mine point which is pointed by the user. The difficulty was how we find the correct game object in a 3D world according to a 2D clicked point. The answer was using **raycasting**.

```c#
public class PlayerInput : MonoBehaviour
{
    void Update()
    {
        if (Input.GetMouseButtonDown(0)) {
            Vector3 position = Input.mousePosition;
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit)) {
                GameObject hitObject = hit.transform.gameObject;
                MinePoint point = hitObject.GetComponent<MinePoint>();
                if (point != null) {
                    PlayerAI ai = GetComponent<PlayerAI>();
                    ai.MoveToPoint(hit.transform.position);
                }
            }
        }
    }
}
```

We can see that the real job of moving was done by another component `PlayerAI`, `PlayerInput` just handled input and direct the AI to move to somewhere.

```c#
enum PlayerState 
{
    Standing,
    Moving,
}

public class PlayerAI : MonoBehaviour
{
    public float speed = 0.5f;

    private CharacterController charController;

    private PlayerState state = PlayerState.Standing;

    private Vector3 nextPosition;

    public void MoveToPoint(Vector3 point)
    {
        if (state == PlayerState.Standing) {
            state = PlayerState.Moving;
            nextPosition = point;
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        charController = GetComponent<CharacterController>();
    }

    // Update is called once per frame
    void Update()
    {
        if (state == PlayerState.Moving) {
            Vector3 direction = new Vector3(
                nextPosition.x - transform.position.x,
                0,
                nextPosition.z - transform.position.z
            );
            direction = Vector3.Normalize(direction);
            Vector3 velocity = direction * speed;
            charController.Move(velocity * Time.deltaTime);

            if (Vector2.Distance(
                new Vector2(transform.position.x, transform.position.z), 
                new Vector2(nextPosition.x, nextPosition.z)) < 0.5) {
                transform.position = new Vector3(nextPosition.x, transform.position.y, nextPosition.z);
                state = PlayerState.Standing;
            }
        }
    }
}
```

{% include image.html name="move.gif" caption="Final visual effect" %}

## A Camera Following the Player

Next, I created a script named `Follower`, which can let the main camera automatically follow the player.

```c#
public class Follower : MonoBehaviour
{
    public GameObject player;

    public float smoothSpeed = 5f;

    private Vector3 forward;

    // Start is called before the first frame update
    void Start()
    {
        forward = player.transform.position - transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void LateUpdate()
    {
        Vector3 nextPos = player.transform.position - forward;
        transform.position = Vector3.Lerp(transform.position, nextPos, smoothSpeed * Time.deltaTime);
    }
}
```

[`LateUpdate`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.LateUpdate.html) is called after all `Update` functions have been called. The logic of moving the camera is usually put in this function since, at that time, all game logics were done. [`Vector3.Lerp`](https://docs.unity3d.com/ScriptReference/Vector3.Lerp.html) linearly interpolates between two vectors, that could make the moving smooth.

{% include image.html name="following.gif" caption="Final visual effect" %}
