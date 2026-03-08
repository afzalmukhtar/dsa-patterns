from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Standard Approach: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        L = 0
        for R in range(len(nums)):
            if nums[R] != val:
                if L != R:
                    nums[L] = nums[R]
                L += 1
        return L

    def removeElementOptimized(self, nums: List[int], val: int) -> int:
        """
        Optimized Approach: Swapping with the End
        
        This is better when elements to remove are rare. 
        Instead of shifting everything left, we swap the target element 
        with the last available element.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                # Replace current element with the last element
                nums[i] = nums[n-1]
                # Reduce array size
                n -= 1
            else:
                i += 1
        return n
