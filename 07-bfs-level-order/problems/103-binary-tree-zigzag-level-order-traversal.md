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

### BFS Approach (Recommended)

The most reliable way to implement Zigzag is to maintain a standard BFS (always processing Left to Right) and simply reverse the order of elements in the current level's list based on a toggle.

1.  **Queue BFS:** Use a standard `deque` to traverse the tree level by level.
2.  **Direction Toggle:** Use a boolean `reverse_level` (initially `False`).
3.  **Process Level:**
    *   Pop all nodes of the current level.
    *   Store their values in a list.
    *   If `reverse_level` is `True`, reverse the list (or use a deque to `appendleft` during the loop).
    *   Append the list to the final result.
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
        level_items = deque() # Using a deque for O(1) prepend
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if reverse_level:
                level_items.appendleft(node.val)
            else:
                level_items.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(list(level_items))
        reverse_level = not reverse_level
        
    return result
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(n)$ - The queue can hold up to $n/2$ nodes.
