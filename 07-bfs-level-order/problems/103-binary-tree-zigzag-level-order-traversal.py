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
        BFS (Breadth-First Search) with Zigzag Toggle
        To perform a zigzag traversal, we use a standard level-order BFS 
        but use a boolean to toggle the insertion direction at each level.
        
        Using a deque for current_level_result ensures O(1) insertions at 
        both ends, maintaining overall O(n) time complexity.
        
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(m) - Max width of the tree.
        """
        if not root:
            return []
        
        from collections import deque

        queue = deque([root])
        result = []

        reverse_level = False
        
        while queue:
            current_level_size = len(queue)
            current_level_result = deque()

            for _ in range(current_level_size):
                node = queue.popleft()

                if reverse_level:
                    current_level_result.appendleft(node.val)
                else:
                    current_level_result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            reverse_level = not reverse_level
            result.append(list(current_level_result))
            
        return result
