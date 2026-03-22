from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS (Breadth-First Search) Approach
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(n) - The maximum width of the tree.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            level_items = []

            for _ in range(level_size):
                node = queue.popleft()
                level_items.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level_items)
            
        return result
