from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Variable-Size Sliding Window
        
        This problem asks for the longest subarray with at most k zeros.
        We maintain a window [L, R] and expand R. If zero count exceeds k,
        shrink from L.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        L = 0
        max_size = 0
        zeroes_flipped = 0  # Number of 0s currently in the window

        for R in range(len(nums)):
            # Expand the window
            if nums[R] == 0:
                zeroes_flipped += 1
            
            # Shrink the window until it is valid (zero count <= k)
            while zeroes_flipped > k:
                if nums[L] == 0:
                    zeroes_flipped -= 1
                L += 1
                
            # Update maximum window size
            max_size = max(max_size, R - L + 1)
            
        return max_size
