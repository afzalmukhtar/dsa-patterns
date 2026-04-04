from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        index_map = {v: i for i, v in enumerate(nums1)}

        stack = [] # stores index not values

        for index in range(len(nums2)):
            while stack and nums2[index] > nums2[stack[-1]]:
                indx = stack.pop()
                if nums2[indx] in index_map:
                    result[index_map[nums2[indx]]] = nums2[index]
            
            stack.append(index)
            
        return result
