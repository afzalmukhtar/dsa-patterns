# Pattern 14A: BFS on Graphs — Shortest Path (Unweighted)

> **Status:** 🔄 In Progress | **Problems Solved:** 0

---

## 1. What is it?
You have a set of nodes connected by edges. BFS (Breadth-First Search) explores the graph layer by layer — all neighbors at distance 1 first, then distance 2, then distance 3, and so on.
Because it expands outward in rings, the first time BFS reaches a node, it has taken the **shortest possible path** to get there — in an unweighted graph.

## 2. When do I use it?
Look for these signals in a problem:
| Signal in the problem | Why BFS |
| :--- | :--- |
| "Find the shortest path" or "minimum steps" | BFS guarantees shortest path in unweighted graphs |
| "Minimum number of moves/operations" | Each BFS level = 1 move |
| "Spread from a source" (fire, infection, rot) | Multi-source BFS |
| Grid with walls/obstacles, find shortest route | Classic BFS on 2D grid |
| Word transformation chains (word ladder) | Each transform = 1 edge |

**The core trigger:** "Minimum steps" + unweighted connections → BFS, immediately.

## 3. The Mental Model
Imagine you drop a stone into still water. The ripples expand outward in perfect circles. BFS is that ripple. The moment a ripple first touches a node, that's the shortest distance to it.
Queue processing mimics this perfectly because it's First-In-First-Out (FIFO).

## 4. Graph Representation
Adjacency List (what you'll almost always use):
```python
edges = [[0,1],[0,2],[1,3],[2,4]]
n = 5  # number of nodes

graph = {i: [] for i in range(n)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected: add both directions
```

## 5. The Critical Rule — Mark visited WHEN ENQUEUING
If you mark visited when dequeuing, the same node can be enqueued multiple times before it's processed, causing duplicate work and incorrect distances.
**✅ RIGHT:**
```python
   mark v as visited   ← the moment you decide to enqueue it
   enqueue v
```

## 6. The Template (Shortest Path)
```python
from collections import deque

def bfs_shortest_path(graph, source, target):
    if source == target: return 0
    
    visited = set([source])
    queue = deque([(source, 0)])   # (node, distance)
    
    while queue:
        node, dist = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == target:
                return dist + 1          # found it — earliest possible = shortest
            
            if neighbor not in visited:
                visited.add(neighbor)    # mark when enqueuing ← critical
                queue.append((neighbor, dist + 1))
    
    return -1   # target not reachable
```

## 7. Multi-Source BFS (Important Variant)
When "multiple starting points spread simultaneously" (e.g. rotting oranges).
**The trick:** seed the queue with ALL sources at distance 0 before you begin.
```python
queue = deque()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 2:           # all rotten oranges are sources
            queue.append((r, c, 0))
            visited.add((r, c))
# Now run BFS normally
```
This works because BFS respects distance ordering. All sources are at distance 0, so they all expand in the same "wave."

---

## 🗂️ Practice Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1971 | Find if Path Exists in Graph | Easy | Just BFS reachability, no distances. |
| 994 | Rotting Oranges | Medium | Multi-source BFS on a grid. |
| 542 | 01 Matrix | Medium | Multi-source BFS: find distance from every cell to nearest 0. |
| 127 | Word Ladder | Hard | BFS where "graph" is implicit. |
| 1091 | Shortest Path in Binary Matrix | Medium | BFS on grid with 8-directional movement. |
