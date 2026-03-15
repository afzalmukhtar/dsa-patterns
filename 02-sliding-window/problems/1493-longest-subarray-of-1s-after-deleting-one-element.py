from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Variable-Size Sliding Window
        
        We allow at most one 0 in the window. When count of 0s > 1, 
        shrink from left. The result is window size - 1 (since 
        we must delete one element).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        L = 0
        max_size = 0
        count = 0  # Count of zeros in the window
        
        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1

            # While window is invalid (contains more than one zero)
            while count > 1:
                if nums[L] == 0:
                    count -= 1
                L += 1
            
            # The current window [L, R] has at most one 0.
            # Its size is R - L + 1. We delete one element, so length is R - L.
            max_size = max(max_size, R - L)
        
        return max_size
