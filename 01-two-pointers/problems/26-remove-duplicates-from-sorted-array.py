from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Original Approach: Using a Hash Set
        Time Complexity: O(n)
        Space Complexity: O(n) - The set stores up to N elements.
        """
        L = 0
        seen = set()

        for R in range(len(nums)):
            if nums[R] not in seen:
                nums[L] = nums[R]
                L += 1
                seen.add(nums[R])
        return L

    def removeDuplicatesOptimized(self, nums: List[int]) -> int:
        """
        Optimized Approach: Pure Two Pointers (O(1) Space)
        Time Complexity: O(n)
        Space Complexity: O(1) - No extra data structure used.
        
        Since the array is sorted, we only need to compare the current 
        element with the last unique element we placed (at L-1).
        """
        if not nums:
            return 0
            
        L = 1  # Next position to fill
        for R in range(1, len(nums)):
            # If the current element is different from the previous unique element
            if nums[R] != nums[L-1]:
                nums[L] = nums[R]
                L += 1
        return L

    def removeDuplicatesGeneral(self, nums: List[int]) -> int:
        """
        General Solution: Template for "at most k" duplicates
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        This template can be adjusted for variations where at most k+1 
        duplicates are allowed (e.g., k=0 for unique, k=1 for at most 2).
        """
        if not nums:
            return 0
            
        L = 0
        n = len(nums)
        k = 0 # additional duplicates allowed (k=0 means each element once)

        for R in range(1, n):
            # If L < k, we are still filling the initial allowed duplicates
            # If nums[R] != nums[L - k], it's a new element or within the limit
            if L < k or nums[R] != nums[L - k]:
                L += 1
                nums[L] = nums[R]
            
        return L + 1
