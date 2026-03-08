from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag Algorithm (Three-Way Partitioning)
        Time Complexity: O(n) - One pass
        Space Complexity: O(1) - In-place modification
        
        Pointers:
        - L (Left): Boundaries for 0s (Red)
        - M (Middle): Current element being scanned
        - R (Right): Boundaries for 2s (Blue)
        """
        L = 0
        M = 0
        R = len(nums) - 1

        while M <= R:
            if nums[M] == 0:
                # If current is 0, swap with Left pointer and advance both
                nums[L], nums[M] = nums[M], nums[L]
                L += 1
                M += 1
            elif nums[M] == 1:
                # If current is 1, it's already in the middle, just advance
                M += 1
            else:
                # If current is 2, swap with Right pointer and decrement R
                # We don't advance M because the swapped element from R 
                # needs to be checked.
                nums[M], nums[R] = nums[R], nums[M]
                R -= 1
