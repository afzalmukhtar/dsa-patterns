# 199. Binary Tree Right Side View

**Difficulty:** Medium

**Topics:** Binary Tree, BFS (Breadth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### Examples

**Example 1:**
- **Input:** `root = [1,2,3,null,5,null,4]`
- **Output:** `[1,3,4]`

**Example 2:**
- **Input:** `root = [1,2,3,4,null,null,null,5]`
- **Output:** `[1,3,4,5]`

**Example 3:**
- **Input:** `root = [1,null,3]`
- **Output:** `[1,3]`

**Example 4:**
- **Input:** `root = []`
- **Output:** `[]`

### Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

### BFS Approach

The right side view of a binary tree is essentially the last node of each level in a level-order traversal.

1.  **Initialize:** Use a queue to perform a standard BFS level-order traversal.
2.  **Iterate:** For each level:
    *   Record the number of nodes at the current level (`level_size`).
    *   Iterate through the nodes of that level.
    *   **Capture the Rightmost Node:** If the current node is the last node in the level (i.e., its index is `level_size - 1`), add its value to the result list.
    *   Add child nodes (left then right) to the queue for the next level.
3.  **Return:** The collected list of values represents the nodes visible from the right side.

```python
from collections import deque

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # If it's the last node in the current level, it's visible from the right
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return result
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(n)$ - In the worst case (a full binary tree), the queue can store up to $n/2$ nodes.
