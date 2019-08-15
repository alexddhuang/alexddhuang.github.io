---
title: "Reading Unity in Action, 2nd Edition"
category: IT
tags: unity game-development csharp
toc: true
---

[Joseph Hocking](http://www.newarteest.com/)'s [*Unity in Action*, 2nd Edition](https://www.manning.com/books/unity-in-action-second-edition) was published in 2018. I choose it as my first book for learning [Unity](https://unity.com/). All of the sample projects from the book can be found on [GitHub](https://github.com/jhocking/uia-2e). I have forked that repo and created a [`playground`](https://github.com/alexddhuang/uia-2e/tree/playground) branch so that I can safely build these projects step-by-step.

## Part 1. First steps

### Chapter 2. Building a demo that puts you in 3D space

#### 2.2 Begin the project: place objects in the scene

We use a Capsule game object to represent the player in this chapter. The Capsule object has a default [Capsule Collider](https://docs.unity3d.com/Manual/class-CapsuleCollider.html) component, we need to replace it with the [Character Controller](https://docs.unity3d.com/Manual/class-CharacterController.html) componenet. Why? 

> The traditional Doom-style first person controls are not physically realistic. The character runs 90 miles per hour, comes to a halt immediately and turns on a dime. Because it is so unrealistic, use of Rigidbodies and physics to create this behavior is impractical and will feel wrong. The solution is the specialized Character Controller. It is simply a capsule shaped Collider which can be told to move in some direction from a script. The Controller will then carry out the movement but be constrained by collisions. It will slide along walls, walk up stairs (if they are lower than the Step Offset) and walk on slopes within the Slope Limit.
> 
> -- [Character Controller \| Unity Docs](https://docs.unity3d.com/Manual/class-CharacterController.html)

#### 2.4 Script component for looking around: `MouseLook`

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


#### 2.5 Keyboard input component: first-person controls

I think the names of variables in the author's original script is not very natural, so I have written my version:

```c#
public class FPSInput : MonoBehaviour
{
    public float speed = 6.0f;

    private CharacterController _charController;

    // Start is called before the first frame update
    void Start()
    {
        _charController = GetComponent<CharacterController>();
    }

    // Update is called once per frame
    void Update()
    {
        float velocityX = Input.GetAxis("Horizontal") * speed;
        float velocityZ = Input.GetAxis("Vertical") * speed;
        Vector3 velocity = new Vector3(velocityX, 0, velocityZ);
        velocity = Vector3.ClampMagnitude(velocity, speed);
        velocity = transform.TransformDirection(velocity);
        velocity.y = 0;
        
        _charController.Move(velocity * Time.deltaTime);
    }
}
```

We invoke [`Vector3.ClampMagnitude`](https://docs.unity3d.com/ScriptReference/Vector3.ClampMagnitude.html) is promising the magnitude of velocity won't exceed the set speed. [`Transform.TransformDirection`](https://docs.unity3d.com/ScriptReference/Transform.TransformDirection.html) transforms a direction from local space to world space. Then we let `velocity.y` equal to zero so that the player will always stick on the ground.

### Chapter 3. Adding enemies and projectiles to the 3D game

#### 3.1 Shooting via raycasts

> Raycasting is when you create a ray and then determine what intersects that ray.

`RayShooter` is a script bound to the camera:

```c#
public class RayShooter : MonoBehaviour
{
    private Camera _camera;

    // Start is called before the first frame update
    void Start()
    {
        _camera = GetComponent<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0)) {
            Vector3 point = new Vector3(_camera.pixelWidth / 2, _camera.pixelHeight / 2, 0);
            Ray ray = _camera.ScreenPointToRay(point);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit)) {
                Debug.Log("Hit " + hit.point);
            }
        }
    }
}
```

[`ScreenPointToRay`](https://docs.unity3d.com/ScriptReference/Camera.ScreenPointToRay.html) returns a ray starting on the near plane of the camera and going from camera through a screen point. Resulting ray is in world space. [`Physics.Raycast`](https://docs.unity3d.com/ScriptReference/Physics.Raycast.html) does the hard calculation of detecting intersections.

Next step, create a sphere at the hit point:

```c#
void Update()
{
    if (Input.GetMouseButtonDown(0)) {
        Vector3 point = new Vector3(_camera.pixelWidth / 2, _camera.pixelHeight / 2, 0);
        Ray ray = _camera.ScreenPointToRay(point);
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit)) {
            Debug.Log("Hit " + hit.point);
            StartCoroutine(SphereIndicator(hit.point));
        }
    }
}

private IEnumerator SphereIndicator(Vector3 pos) 
{
    GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
    sphere.transform.position = pos;

    yield return new WaitForSeconds(1.0f);

    Destroy(sphere);
}
```

[`StartCoroutine`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.StartCoroutine.html) starts a coroutine. The execution of a coroutine can be paused at any point using the `yield` statement. When a `yield` statement is used, the coroutine will pause execution and automatically resume at the next frame.

#### 3.2 Scripting reactive targets

`ReactiveTarget`:

```c#
public class ReactiveTarget : MonoBehaviour
{
    public void ReactToHit()
    {
        StartCoroutine(Die());
    }

    private IEnumerator Die() 
    {
        this.transform.Rotate(-75, 0, 0);

        yield return new WaitForSeconds(1.5f);
        
        Destroy(this.gameObject);
    }
}
```

Then, modify `RayChooter` to invoke `ReactToHit` when a ray hit an enemy.

```c#
if (Physics.Raycast(ray, out hit)) {
    GameObject hitObject = hit.transform.gameObject;
    ReactiveTarget target = hitObject.GetComponent<ReactiveTarget>();
    if (target != null) {
        Debug.Log("Hit " + hit.point);
        target.ReactToHit();
    } else {
        StartCoroutine(SphereIndicator(hit.point));
    }
}
```

#### 3.3 Basic wandering AI

`WanderingAI`:

```c#
public class WanderingAI : MonoBehaviour
{
    public float speed = 3.0f;
    public float obstacleRange = 5.0f;

    private bool _alive;

    public void SetAlive(bool alive) {
        _alive = alive;
    }

    // Start is called before the first frame update
    void Start()
    {
        _alive = true;
    }

    // Update is called once per frame
    void Update()
    {
        if (!_alive) return;
        
        transform.Translate(0, 0, speed * Time.deltaTime);

        Ray ray = new Ray(transform.position, transform.forward);
        RaycastHit hit;
        if (Physics.SphereCast(ray, 0.75f, out hit)) {
            if (hit.distance < obstacleRange) {
                float angle = Random.Range(-110, 110);
                transform.Rotate(0, angle, 0);
            }
        }
    }   
}
```

Being different from `Raycast`, which casts a point along a ray, [`Physics.SphereCast`](https://docs.unity3d.com/ScriptReference/Physics.SphereCast.html) casts a sphere along a ray.

Next step, in `ReactiveTarget.ReactToHit`, we need to set the wandering AI not alive so that it won't continue to move:

```c#
public void ReactToHit()
{
    WanderingAI ai = GetComponent<WanderingAI>();
    if (ai != null) {
        ai.SetAlive(false);
    }
    StartCoroutine(Die());
}
```

#### 3.4 Spawning enemy prefabs

We use an invisible `SceneController` to spawn enemies:

```c#
public class SceneController : MonoBehaviour
{
    [SerializeField] private GameObject enemyPrefab;
    private GameObject _enemy;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (_enemy == null) {
            _enemy = Instantiate(enemyPrefab) as GameObject;
            _enemy.transform.position = new Vector3(0, 1, 0);
            float angle = Random.Range(0, 360);
            _enemy.transform.Rotate(0, angle, 0);
        }
    }
}
```

We can immediately ask a question: Is it possible to happen that `_enemy == null` since there is no place where we assign a `null` to the `_enemy` reference? Recall that in [`ReactiveTarget.Die()`](#32-scripting-reactive-targets), it destroys itself by invoking [`Destroy(this.gameObject)`](https://docs.unity3d.com/ScriptReference/Object.Destroy.html). This method tells the game engine to remove a game object from the scene, but the object may be still available in the memory since C# uses garbage collection to manage memory. However, Unity also overloads the `==` operator to return true when checking for `null` in this situation. Maybe, Unity should provides a property for each game object to indicate whether it is destroyed, so that `_enemy == null` can be replaced by a less confused expression `_enemy.isDestroyed`.

What if we want to spawn not only one enemy?

```c#
void Start()
{
    StartCoroutine(SpawnEnemies());
}

// Update is called once per frame
void Update()
{

}

private IEnumerator SpawnEnemies() {
    GameObject enemy = Instantiate(enemyPrefab) as GameObject;
    enemy.transform.position = new Vector3(0, 1, 0);
    float angle = Random.Range(0, 360);
    enemy.transform.Rotate(0, angle, 0);

    yield return new WaitForSeconds(3f);

    StartCoroutine(SpawnEnemies());
}
```

#### 3.5 Shooting by instantiating objects

Shooting with raycasting is instantaneous, but this time enemies are going to emit fireballs that fly through the air, so that the player has a chance to dodge out of the way.

First, create a prefab named `Fireball`, and create a script also named `Fireball` bound to it.

```c#
public class Fireball : MonoBehaviour
{
    public float speed = 10.0f;
    public int damage = 1;

    // Update is called once per frame
    void Update()
    {
        transform.Translate(0, 0, speed * Time.deltaTime);
    }

    void OnTriggerEnter(Collider other) {
        PlayerCharacter player = other.GetComponent<PlayerCharacter>();
        if (player != null) {
            Debug.Log("Player hit");
            player.Hurt(damage);
        }
        Destroy(this.gameObject);
    }
}
```

To make `OnTriggerEnter` will be called, we have to check the Is Trigger of the Collider component on the fireball.

Next, modify `WanderingAI` to fire when it discovers the player:

```c#
if (Physics.SphereCast(ray, 0.75f, out hit)) {
    if (hit.distance < obstacleRange) {
        GameObject hitObject = hit.transform.gameObject;
        if (hitObject.GetComponent<PlayerCharacter>()) {
            _fireball = Instantiate(fireballPrefab) as GameObject;
            _fireball.transform.position = transform.TransformPoint(Vector3.forward * 1.5f);
            _fireball.transform.rotation = transform.rotation;
        } else {
            float angle = Random.Range(-110, 110);
            transform.Rotate(0, angle, 0);
        }
    }
}
```

### Chapter 4. Developing graphics for your game

#### 4.2 Building basic 3D scenery: whiteboxing

A powerful tool for level editing: [SabreCSG](https://sabrecsg.com/).

#### 4.3 Texture the scene with 2D images

> Technically, textures aren’t applied to geometry directly. Instead, textures can be part of materials, and materials are applied to geometry.

