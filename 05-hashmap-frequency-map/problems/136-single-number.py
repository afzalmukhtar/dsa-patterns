from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Bit Manipulation (XOR) Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        This is the most efficient approach and satisfies the O(1) space constraint.
        a ^ 0 = a
        a ^ a = 0
        a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        """
        res = 0
        for n in nums:
            res ^= n
        return res

    def singleNumber_counter(self, nums: List[int]) -> int:
        """
        Frequency Map Approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Straightforward but uses extra space.
        """
        from collections import Counter
        counts = Counter(nums)
        for num, count in counts.items():
            if count == 1:
                return num
        return -1
