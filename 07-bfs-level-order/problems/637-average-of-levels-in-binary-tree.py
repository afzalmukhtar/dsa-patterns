from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        BFS (Breadth-First Search) Approach
        To find the average of levels, we perform a level-order traversal and 
        calculate the average for each level.
        
        Time Complexity: O(n) - We visit each node once.
        Space Complexity: O(m) - Where m is the maximum width of the tree.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # The average of the current level
            result.append(current_level_sum / level_size)

        return result

    def averageOfLevels_Template(self, root: Optional[TreeNode]) -> List[float]:
        """
        Standard BFS Level-Order Template approach.
        This follows the common pattern of storing all level items first.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level_items = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level_items.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Average calculated using the collected list
            result.append(sum(current_level_items) / level_size)

        return result
