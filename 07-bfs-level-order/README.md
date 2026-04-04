# Pattern #8: BFS / Level Order Traversal

> **Status:** 🔄 In Progress | **Solved:** 6

---

## 1. What is it?
**BFS (Breadth-First Search)** is a way of exploring a tree or graph layer by layer. You visit everything 1 step away first, then everything 2 steps away, and so on. It’s like searching in "ripples."

## 2. When do I use it?
Look for these signals:
- **Shortest Path:** In an **unweighted** graph or grid.
- **Level Order:** "Process nodes layer by layer."
- **Minimum Steps:** "What is the minimum number of moves/transformations?"
- **Nearest/Closest:** "Find the distance to the nearest X."
- **Trigger:** "Find the shortest path in an unweighted graph."

## 3. The Mental Model
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
| 1 | Binary Tree Level Order Traversal | Medium | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| 2 | Rotting Oranges | Medium | [./problems/994-rotting-oranges.md](./problems/994-rotting-oranges.md) ([Sol](./problems/994-rotting-oranges.py)) |
| 3 | 01 Matrix | Medium | [LC 542](https://leetcode.com/problems/01-matrix/) |
| 4 | Minimum Genetic Mutation | Medium | [LC 433](https://leetcode.com/problems/minimum-genetic-mutation/) |
| 5 | Map of Highest Peak | Medium | [LC 1765](https://leetcode.com/problems/map-of-highest-peak/) |
| 6 | Word Ladder | Hard | [LC 127](https://leetcode.com/problems/word-ladder/) |
| 7 | Bus Routes | Hard | [LC 815](https://leetcode.com/problems/bus-routes/) |
