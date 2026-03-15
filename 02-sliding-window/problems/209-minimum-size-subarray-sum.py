from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Variable-Size Sliding Window
        
        Time Complexity: O(n) - Each element is added once and removed once at most.
        Space Complexity: O(1)
        """
        L = 0
        window_sum = 0
        min_size = float("inf")
        
        for R in range(len(nums)):
            window_sum += nums[R]

            # Shrink the window from the left as long as the condition sum >= target is met
            while window_sum >= target:
                min_size = min(min_size, R - L + 1)
                window_sum -= nums[L]
                L += 1
                
        return min_size if min_size != float("inf") else 0
