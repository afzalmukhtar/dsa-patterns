from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The core idea: For each bar i, we want to find the largest rectangle that 
        INCLUDES this bar as the shortest bar.
        To do this, we need to know how far the rectangle can extend to the LEFT 
        and RIGHT until it hits a bar SHORTER than heights[i].
        
        - left[i]: index of the first bar to the left that is shorter than heights[i].
        - right[i]: index of the first bar to the right that is shorter than heights[i].
        
        Width of the rectangle using heights[i] as height = (right[i] - left[i] - 1).
        """
        n = len(heights)
        left = [-1] * n  # Default to -1 if no shorter bar exists on the left
        right = [n] * n  # Default to n if no shorter bar exists on the right
        stack = []

        # Find First Smaller Element to the RIGHT
        # We use a Monotonic Increasing Stack. 
        # If the incoming bar is shorter than the top, it 'resolves' the top's right boundary.
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)
        
        stack.clear()

        # Find First Smaller Element to the LEFT
        # We traverse backwards.
        # If the incoming bar (on the left) is shorter than the top, it 'resolves' the top's left boundary.
        for i in range(n - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                left[idx] = i
            stack.append(i)

        area = 0
        for index in range(n):
            # Area = height * (right_boundary - left_boundary - 1)
            area = max(area, (right[index] - left[index] - 1) * heights[index])

        return area
