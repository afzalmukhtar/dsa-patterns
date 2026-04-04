from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n

        # Process the array twice to simulate circularity
        for i in range(n * 2):
            # i % n gives the "virtual" index in the circular array
            while stack and nums[i % n] > nums[stack[-1]]:
                indx = stack.pop()
                result[indx] = nums[i % n]
            
            # We only add to the stack during the first pass (i < n)
            # because we only need to find the NGE for the n elements.
            if i < n:
                stack.append(i)
                
        return result
