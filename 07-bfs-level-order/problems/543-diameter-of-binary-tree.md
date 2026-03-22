# 543. Diameter of Binary Tree

**Difficulty:** Easy

**Topics:** Binary Tree, DFS (Depth-First Search)

---

### Problem Statement

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

### Examples

**Example 1:**
- **Input:** `root = [1,2,3,4,5]`
- **Output:** `3`
- **Explanation:** 3 is the length of the path `[4,2,1,3]` or `[5,2,1,3]`.

**Example 2:**
- **Input:** `root = [1,2]`
- **Output:** `1`

### Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

### DFS Approach (Bottom-Up)

The diameter of a tree at a specific node is the sum of the heights of its left and right subtrees. We can use a recursive DFS to calculate the height of each node while simultaneously updating a global `diameter` variable.

1.  **Recursive Function:** Define a function `dfs(node)` that returns the **height** of the node.
2.  **Base Case:** If the node is `None`, its height is 0.
3.  **Recursive Step:**
    *   Calculate `leftHeight = dfs(node.left)`.
    *   Calculate `rightHeight = dfs(node.right)`.
    *   **Update Diameter:** The potential diameter passing through the current node is `leftHeight + rightHeight`. Update the global maximum if this sum is larger.
    *   **Return Height:** Return `1 + max(leftHeight, rightHeight)` to the parent.

```python
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(node):
        if not node:
            return 0
        
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)
        
        nonlocal diameter
        # Update diameter with path through current node
        diameter = max(diameter, leftHeight + rightHeight)
        
        # Return height of current node
        return 1 + max(leftHeight, rightHeight)
    
    dfs(root)
    return diameter
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(h)$ - Height of the tree (stack space for recursion).
