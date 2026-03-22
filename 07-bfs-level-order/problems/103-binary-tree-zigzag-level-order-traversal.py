from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS (Breadth-First Search) with Direction Toggle
        To handle the zigzag pattern, we perform a standard level-order 
        traversal but use a boolean flag to decide whether to prepend 
        or append elements to the current level's result list.
        
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(m) - Max width of the binary tree.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []
        reverse_level = False
        
        while queue:
            level_size = len(queue)
            # Use deque for O(1) prepend when we need to reverse the level
            level_items = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Depending on the zigzag direction, append or prepend
                if reverse_level:
                    level_items.appendleft(node.val)
                else:
                    level_items.append(node.val)
                
                # Standard BFS always adds children left-to-right to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level_items))
            # Flip the direction for the next level
            reverse_level = not reverse_level
            
        return result
