from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Variable-Size Sliding Window (Counting Pattern)
        
        We maintain a window [L, R] such that the product of elements 
        is strictly less than k. For each new R, we expand and then 
        shrink from L if needed. 
        
        The number of subarrays ending at R that satisfy the condition 
        is (R - L + 1).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Edge case: If k <= 1, no subarray can have product < k (since nums[i] >= 1)
        if k <= 1:
            return 0
            
        L = 0
        count = 0
        product = 1

        for R in range(len(nums)):
            # Expand the window
            product *= nums[R]

            # Shrink the window until the condition (product < k) is met
            while product >= k:
                product //= nums[L]
                L += 1
            
            # Every subarray ending at R in the range [L, R] is valid.
            # There are exactly R - L + 1 such subarrays.
            count += R - L + 1
            
        return count
