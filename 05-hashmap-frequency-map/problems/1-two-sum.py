from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Map Approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        We iterate through the array once. For each element, we calculate its 
        complement (target - nums[i]) and check if it already exists in our 
        hash map (which stores values and their indices).
        """
        index_map = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_map:
                return [index_map[complement], i]
            index_map[nums[i]] = i

        return [-1, -1]
