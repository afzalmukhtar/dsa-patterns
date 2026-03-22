# 637. Average of Levels in Binary Tree

**Difficulty:** Easy

**Topics:** Binary Tree, BFS (Breadth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within $10^{-5}$ of the actual answer will be accepted.

### Examples

**Example 1:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[3.00000, 14.50000, 11.00000]`
- **Explanation:** The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.

**Example 2:**
- **Input:** `root = [3,9,20,15,7]`
- **Output:** `[3.00000, 14.50000, 11.00000]`

### Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- $-2^{31} <= Node.val <= 2^{31} - 1$

---

### BFS Approach

This problem is a direct application of the level-order traversal pattern. We visit nodes level by level and calculate the average for each level.

#### Approach 1: Standard BFS Template (Storing Level Items)
This approach follows the general template where we collect all items of a level into a list first.

```python
from collections import deque

def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level_items = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_items.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Calculate average using the collected list
        result.append(sum(current_level_items) / level_size)
        
    return result
```

#### Approach 2: Optimized Space (Running Sum)
Instead of storing all values of a level in a list, we can maintain a running sum. This is more space-efficient as it avoids creating a new list for every level.

```python
from collections import deque

def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Calculate average using the running sum
        result.append(current_level_sum / level_size)
        
    return result
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(m)$ - Where $m$ is the maximum number of nodes at any level (the maximum width of the tree).
