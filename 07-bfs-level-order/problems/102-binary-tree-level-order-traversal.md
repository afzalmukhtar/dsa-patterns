# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium

**Topics:** Binary Tree, BFS (Breadth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Examples

**Example 1:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[3],[9,20],[15,7]]`

**Example 2:**
- **Input:** `root = [1]`
- **Output:** `[[1]]`

**Example 3:**
- **Input:** `root = []`
- **Output:** `[]`

### Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

### BFS Approach

The level order traversal is naturally solved using BFS. We use a queue to keep track of the nodes at each level.

1.  **Initialize:** Start by adding the root to a queue.
2.  **Iterate:** While the queue is not empty:
    *   Get the current size of the queue (this represents the number of nodes at the current level).
    *   Iterate through that many nodes, popping them from the front of the queue.
    *   Add each node's value to a level list.
    *   Add each node's children (left then right) back into the queue for the next level.
3.  **Result:** Append each level list to our final result.

```python
from collections import deque

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        level_items = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_items.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_items)
        
    return result
```

- **Time Complexity:** $O(n)$ - We visit each node once.
- **Space Complexity:** $O(n)$ - In the worst case (a full binary tree), the queue will hold up to $n/2$ nodes at the leaf level.
