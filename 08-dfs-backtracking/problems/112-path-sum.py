from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum_DFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Recursive DFS approach (User Provided).
        Time: O(n), Space: O(h)
        """
        if not root:
            return False
        
        remaining = targetSum - root.val

        if not root.left and not root.right:
            return remaining == 0
        
        return self.hasPathSum_DFS(root.left, remaining) or self.hasPathSum_DFS(root.right, remaining)

    def hasPathSum_BFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Iterative BFS approach (Level Order with Running Sum).
        Each queue item is (node, current_path_sum).
        Time: O(n), Space: O(m)
        """
        if not root:
            return False
        
        queue = deque([(root, root.val)])
        
        while queue:
            node, current_sum = queue.popleft()
            
            # If it's a leaf, check the sum
            if not node.left and not node.right:
                if current_sum == targetSum:
                    return True
            
            if node.left:
                queue.append((node.left, current_sum + node.left.val))
            if node.right:
                queue.append((node.right, current_sum + node.right.val))
                
        return False

    # Default implementation
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        remaining = targetSum - root.val

        if not root.left and not root.right:
            return remaining == 0
        
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
