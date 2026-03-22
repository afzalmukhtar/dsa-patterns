from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS approach.
        Time: O(n), Space: O(h)
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth_DFS(root.left), self.maxDepth_DFS(root.right))

    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach (Level Order Traversal).
        In BFS, max depth is the total number of levels.
        Time: O(n), Space: O(m) where m is the max width of the tree.
        """
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

    # Default implementation using the user-provided recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
