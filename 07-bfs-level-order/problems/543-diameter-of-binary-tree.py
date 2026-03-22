from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS (Depth-First Search) Bottom-Up Approach
        To find the diameter, we need the height of each node. The diameter 
        at any node is the sum of the heights of its left and right children.
        
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(h) - Call stack for recursion.
        """
        diameter = 0

        def dfs(node):
            if node is None:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            nonlocal diameter

            # Update diameter with the longest path through this node
            diameter = max(diameter, leftHeight + rightHeight)

            # Return the height of this node to its parent
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return diameter
