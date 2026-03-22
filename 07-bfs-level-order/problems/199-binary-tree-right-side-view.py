from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS (Breadth-First Search) Approach
        To find the right side view, we perform a level-order traversal and 
        capture the value of the last node at each level.
        
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(n) - The maximum width of the tree.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node of the current level, add it to result
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return result
