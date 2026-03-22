from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        DFS Bottom-Up Approach (Optimized)
        A binary tree is balanced if for every node, its left and right 
        subtrees differ in height by at most 1.
        
        Using a bottom-up approach, we calculate heights and check 
        balance simultaneously. We return -1 if any subtree is unbalanced.
        
        Time Complexity: O(n) - Every node is visited once.
        Space Complexity: O(h) - Call stack for recursion.
        """
        def dfs(node) -> int:
            if node is None:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            # Propagate the unbalance signal (-1) up the tree
            if leftHeight == -1 or rightHeight == -1:
                return -1
            
            # Check balance at the current node
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Return height if balanced
            return 1 + max(leftHeight, rightHeight)
        
        # A result of -1 means the tree is unbalanced
        return dfs(root) != -1
