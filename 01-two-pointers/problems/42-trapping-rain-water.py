from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Optimal Two Pointers Approach
        
        We use two pointers from both ends and move the one that has the smaller
        maximum height boundary. The water trapped at any point is:
        water = min(max_left, max_right) - height[current]
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0

        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        stored = 0

        while L < R:
            if maxL < maxR:
                L += 1
                # Update maxL and add trapped water
                # If height[L] is greater than maxL, water trapped is 0
                maxL = max(maxL, height[L])
                stored += maxL - height[L]
            else:
                R -= 1
                # Update maxR and add trapped water
                maxR = max(maxR, height[R])
                stored += maxR - height[R]

        return stored
