---
title: "Notes on Tommy Thompson's Pathfinding in Unity Tutorial Series"
date: 2019-08-19 17:07:04 +0800
category: IT
tags: unity csharp game-dev
toc: true
---

Tommy Thompson's [Pathfinding in Unity Tutorial Series](https://aiandgames.com/unity-pathfinding-part-1-nav-mesh-basics/) teaches how we use the navigation tools built into the Unity engine.

## Part 1. Nav Mesh Basics

### Creating a Surface for Navigation

#### Building a Navigation Mesh

Simple steps: Window -> AI -> Navigation. 

In the Object tab, check the Navigation Static box,

> which tells us we want to declare this space as part of the navigation space and it’s not going to change it’s position or move.

Then go to the Bake tab and click the Bake button.

### Creating a Navigation Agent

Add the [`NavMeshAgent`](https://docs.unity3d.com/ScriptReference/AI.NavMeshAgent.html) component to the NPC.

#### Moving a Navigation Agent

`NPCMove`:

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class NPCMove : MonoBehaviour
{
    [SerializeField]
    Transform _destination;

    NavMeshAgent _navMeshAgent;

    // Start is called before the first frame update
    void Start()
    {
        _navMeshAgent = GetComponent<NavMeshAgent>();

        SetDestination();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void SetDestination()
    {
        if (_destination != null) {
            Vector3 targetVector = _destination.transform.position;
            _navMeshAgent.SetDestination(targetVector);
        }
    }
}
```

## Part 2. Nav Mesh Obstacles

### Creating a Nav Mesh Obstacle

Go back to the Object tab, select the obstacle object, click Navigation Static and set Navigation Area to Not Walkable, and then bake again.

#### Changing Obstacle Size

Add component [`NavMeshObstacle`](https://docs.unity3d.com/Manual/class-NavMeshObstacle.html) to the obstacle object. This component can enable us to change the size of the obstacle, but don't forget to tick the Carve checkbox.

## Part 3. Simple Patrols

### A Waypoint Class

```c#
public class Waypoint : MonoBehaviour
{
    [SerializeField]
    float debugDrawRadius = 1.0F;
   
    void OnDrawGizmos()
    {
        Gizmos.color = Color.red;
        Gizmos.DrawWireSphere(transform.position, debugDrawRadius);
    }
}
```

### A Patrolling NPC

```c#
public class NPCSimplePatrol : MonoBehaviour
{
    // Dictates whether the agent waits on each node.
    [SerializeField]
    bool _patrolWaiting;

    [SerializeField]
    float _totalWaitTime = 3f;

    // The probability of switching direction.
    [SerializeField]
    float _switchProbability = 0.2f;

    [SerializeField]
    List<Waypoint> _patrolPoints;

    NavMeshAgent _navMeshAgent;
    int _currentPatrolIndex;
    bool _travelling;
    bool _waiting;
    bool _patrolForward;
    float _waitTimer;

    // Start is called before the first frame update
    void Start()
    {
        _navMeshAgent = GetComponent<NavMeshAgent>();
        
        if (_patrolPoints != null && _patrolPoints.Count >= 2) {
            _currentPatrolIndex = 0;
            SetDestination();
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (_travelling && _navMeshAgent.remainingDistance <= 1.0f) {
            _travelling = false;
            if (_patrolWaiting) {
                _waiting = true;
                _waitTimer = 0f;
            } else {
                ChangePatrolPoint();
                SetDestination();
            }
        }

        if (_waiting) {
            _waitTimer += Time.deltaTime;
            if (_waitTimer >= _totalWaitTime) {
                _waiting = false;
                ChangePatrolPoint();
                SetDestination();
            }
        }
    }

    private void SetDestination()
    {
        if (_patrolPoints != null) {
            Vector3 targetVector = _patrolPoints[_currentPatrolIndex].transform.position;
            _navMeshAgent.SetDestination(targetVector);
            _travelling = true;
        }
    }

    private void ChangePatrolPoint()
    {
        if (Random.Range(0f, 1f) <= _switchProbability) {
            _patrolForward = !_patrolForward;
        }
 
        if (_patrolForward) {
            _currentPatrolIndex = (_currentPatrolIndex + 1) % _patrolPoints.Count;
        }
        else {
            if (--_currentPatrolIndex < 0) {
                _currentPatrolIndex = _patrolPoints.Count - 1;
            }
        }
    }
}
```

## Part 4. Dynamic Patrols

### Building an Adjacency List

```c#
public class ConnectedWaypoint : Waypoint
{
    [SerializeField]
    protected float _connectivityRadius = 50f;
 
    List<ConnectedWaypoint> _connections;

    // Start is called before the first frame update
    void Start()
    {
        // Grab all waypoint objects in scene.
        GameObject[] allWaypoints = GameObject.FindGameObjectsWithTag("Waypoint");

        // Create a list of waypoints I can refer to later.
        _connections = new List<ConnectedWaypoint>();

        // Check if they're a connected waypoint.
        for (int i = 0; i < allWaypoints.Length; i++) {
            ConnectedWaypoint nextWaypoint = allWaypoints[i].GetComponent<ConnectedWaypoint>();
            if (nextWaypoint != null) {
                if(Vector3.Distance(this.transform.position, nextWaypoint.transform.position) <= _connectivityRadius && nextWaypoint != this)
                {
                    _connections.Add(nextWaypoint);
                }
            }
        }
    }

    public void OnDrawGizmos()
    {
        base.OnDrawGizmos();

        Gizmos.color = Color.yellow;
        Gizmos.DrawWireSphere(transform.position, _connectivityRadius);
    }

    public ConnectedWaypoint NextWaypoint(ConnectedWaypoint previousWaypoint)
    {
        if (_connections.Count == 0) {
            Debug.LogError("Insufficient waypoint count.");
            return null;
        } else if (_connections.Count == 1 && _connections.Contains(previousWaypoint)) {
            return previousWaypoint;
        } else {
            ConnectedWaypoint nextWaypoint;
            int nextIndex = 0;

            do {
                nextIndex = Random.Range(0, _connections.Count);
                nextWaypoint = _connections[nextIndex];

            } while (nextWaypoint == previousWaypoint);

            return nextWaypoint;
        }
    }
}
```

### Rewriting the Patrol Agent

```c#
namespace Assets.Code
{
    public class NPCConnectedPatrol: MonoBehaviour
    {
        // Dictates whether the agent waits on each node.
        [SerializeField]
        bool _patrolWaiting;
 
        // The total time we wait at each node.
        [SerializeField]
        float _totalWaitTime = 3f;
 
        // The probability of switching direction.
        [SerializeField]
        float _switchProbability = 0.2f;
 
        // Private variables for base behaviour.
        NavMeshAgent _navMeshAgent;
        ConnectedWaypoint _currentWaypoint;
        ConnectedWaypoint _previousWaypoint;
 
        bool _travelling;
        bool _waiting;
        float _waitTimer;
        int _waypointsVisited;
 
        // Use this for initialization
        public void Start()
        {
            _navMeshAgent = this.GetComponent<NavMeshAgent>();

            if (_currentWaypoint == null) {
                GameObject[] allWaypoints = GameObject.FindGameObjectsWithTag("Waypoint");

                if (allWaypoints.Length > 0) {
                    while (_currentWaypoint == null) {
                        int random = UnityEngine.Random.Range(0, allWaypoints.Length);
                        ConnectedWaypoint startingWaypoint = allWaypoints[random].GetComponent<ConnectedWaypoint>();

                        if (startingWaypoint != null) {
                            _currentWaypoint = startingWaypoint;
                        }
                    }
                } else {
                    Debug.LogError("Failed to find any waypoints for use in the scene.");
                }
            }
            
            SetDestination();
        }
 
        public void Update()
        {
            if (_travelling && _navMeshAgent.remainingDistance <= 1.0f) {
                _travelling = false;
                _waypointsVisited++;

                if (_patrolWaiting) {
                    _waiting = true;
                    _waitTimer = 0f;
                } else {
                    SetDestination();
                }
            }
 
            if (_waiting) {
                _waitTimer += Time.deltaTime;
                if (_waitTimer >= _totalWaitTime) {
                    _waiting = false;
 
                    SetDestination();
                }
            }
        }
 
        private void SetDestination()
        {
            if (_waypointsVisited > 0) {
                ConnectedWaypoint nextWaypoint = _currentWaypoint.NextWaypoint(_previousWaypoint);
                _previousWaypoint = _currentWaypoint;
                _currentWaypoint = nextWaypoint;
            }
           
            Vector3 targetVector = _currentWaypoint.transform.position;
            _navMeshAgent.SetDestination(targetVector);
            _travelling = true;
        }
    }
}
```