from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Original Approach: Two-Pass Logic
        Total writes: Always N (M non-zero assignments + (N-M) zero assignments)
        Total passes: 2
        """
        L = 0
        R = 0
        l = len(nums)
        
        # Pass 1: Move all non-zero elements to the front
        while R < l:
            if nums[R] != 0:
                nums[L] = nums[R]
                L += 1
            R += 1
        
        # Pass 2: Fill the remaining space with zeroes
        while L < l:
            nums[L] = 0
            L += 1

    def moveZeroesOptimized(self, nums: List[int]) -> None:
        """
        Optimized Approach: One-Pass Swap
        Total writes: Minimizes writes by using swaps only when L != R.
        Total passes: 1
        
        This minimizes operations because:
        1. It only performs writes when a non-zero element needs to move.
        2. It avoids a second pass to fill zeros.
        """
        L = 0
        l = len(nums)
        
        for R in range(l):
            if nums[R] != 0:
                # Only swap if the pointers are at different positions
                if L != R:
                    nums[L], nums[R] = nums[R], nums[L]
                L += 1
