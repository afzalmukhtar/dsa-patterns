# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy

**Topics:** Binary Tree, BFS (Breadth-First Search), DFS (Depth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Examples

**Example 1:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `3`

**Example 2:**
- **Input:** `root = [1,null,2]`
- **Output:** `2`

### Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

### Approaches

#### 1. BFS Approach (Level Order Traversal)
Since we are in the BFS pattern, the maximum depth is simply the total number of levels in the tree. We can use a queue to traverse level by level and increment a counter for each level.

```python
from collections import deque

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return depth
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(m)$ - Max width of the tree.

#### 2. Recursive DFS Approach
The depth of a tree is $1 + \max(\text{depth of left child}, \text{depth of right child})$.

```python
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(h)$ - Height of the tree (call stack).
