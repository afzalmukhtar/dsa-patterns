# 112. Path Sum

**Difficulty:** Easy

**Topics:** Binary Tree, BFS (Breadth-First Search), DFS (Depth-First Search)

---

### Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

### Examples

**Example 1:**
- **Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
- **Output:** `true`
- **Explanation:** The root-to-leaf path with the target sum is `5 -> 4 -> 11 -> 2`.

**Example 2:**
- **Input:** `root = [1,2,3], targetSum = 5`
- **Output:** `false`
- **Explanation:** There are two root-to-leaf paths: `(1 -> 2)` sum is 3, and `(1 -> 3)` sum is 4.

**Example 3:**
- **Input:** `root = [], targetSum = 0`
- **Output:** `false`

### Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

---

### Approaches

#### 1. BFS Approach (Level Order)
While BFS is usually used for level-order traversal, it can solve path sum by storing the "running sum" along with each node in the queue.

1.  **Queue:** Store tuples of `(node, current_sum)`.
2.  **Process:** For each node, calculate the sum from root to that node.
3.  **Leaf Check:** If the current node is a leaf and `current_sum == targetSum`, return `true`.

```python
from collections import deque

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    
    # Queue stores (node, sum_from_root_to_node)
    queue = deque([(root, root.val)])
    
    while queue:
        node, current_sum = queue.popleft()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            if current_sum == targetSum:
                return True
        
        if node.left:
            queue.append((node.left, current_sum + node.left.val))
        if node.right:
            queue.append((node.right, current_sum + node.right.val))
            
    return False
```

#### 2. Recursive DFS Approach (User Provided)
This is the most concise approach. We subtract the current node's value from the target sum and check if any path from the children can satisfy the remaining sum.

```python
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    
    remaining = targetSum - root.val
    
    # If leaf node, check if remaining sum is 0
    if not root.left and not root.right:
        return remaining == 0
    
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(h)$ - Height of the tree (stack space for DFS or queue width for BFS).
