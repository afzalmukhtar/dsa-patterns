# 110. Balanced Binary Tree

**Difficulty:** Easy

**Topics:** Binary Tree, DFS (Depth-First Search)

---

### Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

### Examples

**Example 1:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `true`

**Example 2:**
- **Input:** `root = [1,2,2,3,3,null,null,4,4]`
- **Output:** `false`

**Example 3:**
- **Input:** `root = []`
- **Output:** `true`

### Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

---

### DFS Approach (Bottom-Up)

A naive approach would calculate the height of left and right subtrees for every node, resulting in $O(n^2)$ time. An optimized approach uses a bottom-up DFS to check balance while calculating height in a single pass.

1.  **Recursive Function:** Define `dfs(node)` that returns the height of the node if it's balanced, or `-1` if any subtree is unbalanced.
2.  **Base Case:** An empty node has a height of `0`.
3.  **Recursive Step:**
    *   Recursively find `leftHeight = dfs(node.left)`.
    *   Recursively find `rightHeight = dfs(node.right)`.
    *   **Fail Fast:** If either child returned `-1`, the current tree is unbalanced; return `-1`.
    *   **Balance Check:** If `abs(leftHeight - rightHeight) > 1`, return `-1`.
    *   **Return Height:** Otherwise, return the height of the current node: `1 + max(leftHeight, rightHeight)`.

```python
def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node) -> int:
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If subtrees are unbalanced or current node is unbalanced
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
            
        return 1 + max(left, right)
    
    return dfs(root) != -1
```

- **Time Complexity:** $O(n)$ - Every node is visited once.
- **Space Complexity:** $O(h)$ - Height of the tree (stack space).
