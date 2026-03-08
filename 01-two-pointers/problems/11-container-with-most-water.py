from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two Pointers Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        The area is limited by the shorter line. We move the pointer pointing 
        to the shorter line inward to potentially find a taller line that 
        results in a larger area, despite the decreased width.
        """
        L = 0
        R = len(height) - 1
        max_area = 0
        
        while L < R:
            # Area = width * min(height[L], height[R])
            width = R - L
            if height[L] < height[R]:
                current_area = height[L] * width
                L += 1
            else:
                current_area = height[R] * width
                R -= 1
            
            max_area = max(max_area, current_area)
            
        return max_area
