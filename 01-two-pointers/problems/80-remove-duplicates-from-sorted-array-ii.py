from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        General Solution: Template for "at most k+1" duplicates
        In this case, k=1 allows each element to appear at most twice.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
            
        L = 0
        n = len(nums)
        k = 1  # Number of additional duplicates allowed (k=1 means at most 2 of each)

        for R in range(1, n):
            # If we are within the allowed duplication window (L < k)
            # OR the current element is different from the one at the back of the window
            if L < k or nums[R] != nums[L - k]:
                L += 1
                nums[L] = nums[R]
            
        return L + 1
