# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

**Topics:** Binary Tree, BFS (Breadth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

### Examples

**Example 1:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[3],[20,9],[15,7]]`

**Example 2:**
- **Input:** `root = [1]`
- **Output:** `[[1]]`

**Example 3:**
- **Input:** `root = []`
- **Output:** `[]`

### Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

---

### BFS Approach (Zigzag Toggle)

The most efficient way to implement Zigzag is to maintain a standard BFS (always processing Left to Right) and use a double-ended queue (`deque`) to build each level's list. This allows for $O(1)$ insertions at either end based on the current direction.

1.  **Queue BFS:** Use a standard `deque` to traverse the tree level by level.
2.  **Direction Toggle:** Use a boolean `reverse_level` (initially `False`).
3.  **Process Level:**
    *   Create a `current_level_result` as a `deque`.
    *   For each node in the level:
        *   If `reverse_level` is `True`, `appendleft` the value.
        *   Else, `append` the value.
        *   Add children (left then right) to the main BFS queue.
    *   Convert `current_level_result` to a list and append to the final result.
    *   Flip the `reverse_level` toggle.

```python
from collections import deque

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    reverse_level = False
    
    while queue:
        level_size = len(queue)
        current_level_result = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if reverse_level:
                current_level_result.appendleft(node.val)
            else:
                current_level_result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(list(current_level_result))
        reverse_level = not reverse_level
        
    return result
```

- **Time Complexity:** $O(n)$ - Every node is visited once, and each insertion into the level deque is $O(1)$.
- **Space Complexity:** $O(n)$ - The queue can hold up to $n/2$ nodes in the worst case.
