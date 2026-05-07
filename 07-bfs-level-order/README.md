# Pattern #8: BFS / Level Order Traversal

> **Status:** 🔄 In Progress | **Solved:** 9

---

## 1. What is it?
**BFS (Breadth-First Search)** is a way of exploring a tree or graph layer by layer. You visit everything 1 step away first, then everything 2 steps away, and so on. It’s like searching in "ripples."

## 2. Meta-Principle: Where do I start? (Selecting Sources)
The most common confusion with BFS (especially Multi-Source BFS) is: **"Should I start from the 0s or the 1s?"**

The mental rule to always know where to start is:
> **The source is whatever you already know the answer for.**

| Problem | Known Answer (Sources) | Unknown Answer (To be filled) |
| :--- | :--- | :--- |
| **01 Matrix** | Cells with `0` (distance is `0`) | Cells with `1` (what is their distance?) |
| **Rotting Oranges** | Rotten oranges (time is `0`) | Fresh oranges (when do they rot?) |
| **Map of Highest Peak** | Water cells (height is `0`) | Land cells (what is their height?) |

The pattern is always the same:
1. Identify the cells that already have a definite answer of `0` (distance, time, or height).
2. Seed these cells into the `queue` at the beginning.
3. Let BFS spread outward to fill in the unknown cells.

## 3. When do I use it?
Look for these signals:
- **Shortest Path:** In an **unweighted** graph or grid.
- **Level Order:** "Process nodes layer by layer."
- **Minimum Steps:** "What is the minimum number of moves/transformations?"
- **Nearest/Closest:** "Find the distance to the nearest X."
- **Trigger:** "Find the shortest path in an unweighted graph."

## 4. The Mental Model
Imagine dropping a stone in a pond. The ripples expand outward in all directions simultaneously, one layer at a time. BFS uses a **Queue (FIFO)** to maintain the "current ripple front."

```text
Tree:
        1
       / \
      2   3
     / \    \
    4   5    6

BFS order: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Layer 0: [1]
Layer 1: [2, 3]
Layer 2: [4, 5, 6]
```

## 4. Brute Force First
For shortest path, you might try DFS (Depth-First Search). However, DFS explores one path to its very end before trying another.
- **Why it's slow:** DFS might find a very long path first and waste time. To find the *shortest* path with DFS, you'd have to explore **every single path** in the entire graph.

## 5. The Optimization Insight
A **Queue** processes nodes in the exact order they arrived. If you enqueue all neighbors of Level 1, they will *all* be processed before any neighbors of Level 2.
**The "Level Size" Trick:** By taking a snapshot of the queue size at the start of each level, you can process exactly one "ripple" at a time.

## 6. The Optimal Solution
BFS guarantees the shortest path in an unweighted graph because it explores all paths of length $L$ before any path of length $L+1$.
- **Time:** $O(V + E)$ (Vertices + Edges)
- **Space:** $O(V)$ (To store the queue and visited set)

## 7. The Templates

### Template A: Level-Order (Tree/Aware)
```python
from collections import deque
def bfs_level_order(root):
    if not root: return []
    queue = deque([root])
    while queue:
        level_size = len(queue) # Snapshot current level
        for _ in range(level_size):
            node = queue.popleft()
            # Process node...
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
```

### Template B: Graph Shortest Path
```python
def bfs_shortest_path(start, target):
    queue = deque([(start, 0)]) # (node, distance)
    visited = {start}
    while queue:
        curr, dist = queue.popleft()
        if curr == target: return dist
        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```

### Template C: Multi-Source BFS
```python
def multi_source_bfs(sources):
    queue = deque(sources) # Seed ALL sources at distance 0
    visited = set(sources)
    while queue:
        # Expand ripples from all sources simultaneously...
        pass
```

## 8. Variations and Edge Cases
- **Multi-Source BFS:** Used when multiple "fires" or "rots" spread at once (e.g., Rotting Oranges).
- **0-1 BFS:** Used when edges have weights 0 or 1 (use a Deque and `popleft` for 0, `pop` for 1).
- **Visited Set:** Crucial for graphs with cycles to avoid infinite loops. **Always add to `visited` when enqueuing, not dequeuing.**

## 9. Practice Problems

| # | Problem | Difficulty | Link |
|---|---------|------------|------|
| 1 | Binary Tree Level Order Traversal | Medium | [./problems/102-binary-tree-level-order-traversal.md](./problems/102-binary-tree-level-order-traversal.md) ([Sol](./problems/102-binary-tree-level-order-traversal.py)) |
| 2 | Rotting Oranges | Medium | [./problems/994-rotting-oranges.md](./problems/994-rotting-oranges.md) ([Sol](./problems/994-rotting-oranges.py)) |
| 3 | 01 Matrix | Medium | [./problems/542-01-matrix.md](./problems/542-01-matrix.md) ([Sol](./problems/542-01-matrix.py)) |
| 4 | Minimum Genetic Mutation | Medium | [./problems/433-minimum-genetic-mutation.md](./problems/433-minimum-genetic-mutation.md) ([Sol](./problems/433-minimum-genetic-mutation.py)) |
| 5 | Binary Tree Right Side View | Medium | [./problems/199-binary-tree-right-side-view.md](./problems/199-binary-tree-right-side-view.md) ([Sol](./problems/199-binary-tree-right-side-view.py)) |
| 6 | Word Ladder | Hard | [./problems/127-word-ladder.md](./problems/127-word-ladder.md) ([Sol](./problems/127-word-ladder.py)) |
| 7 | Average of Levels in Binary Tree | Easy | [./problems/637-average-of-levels-in-binary-tree.md](./problems/637-average-of-levels-in-binary-tree.md) ([Sol](./problems/637-average-of-levels-in-binary-tree.py)) |
| 8 | Binary Tree Zigzag Level Order Traversal | Medium | [./problems/103-binary-tree-zigzag-level-order-traversal.md](./problems/103-binary-tree-zigzag-level-order-traversal.md) ([Sol](./problems/103-binary-tree-zigzag-level-order-traversal.py)) |
| 9 | Map of Highest Peak | Medium | [./problems/1765-map-of-highest-peak.md](./problems/1765-map-of-highest-peak.md) ([Sol](./problems/1765-map-of-highest-peak.py)) |
