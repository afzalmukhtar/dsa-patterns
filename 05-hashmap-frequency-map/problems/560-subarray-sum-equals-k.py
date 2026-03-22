from typing import List
from collections import Counter

class Solution:
    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        """
        Brute Force Approach
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        
        A nested loop calculates the sum of all possible subarrays.
        """
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Optimal Approach (Prefix Sum + HashMap)
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Insight: 
        If PrefixSum[i] - PrefixSum[j] = k, then the sum of subarray 
        between indices j+1 and i is k.
        Rearranging: PrefixSum[j] = PrefixSum[i] - k
        """
        prefix_map = Counter({0 : 1})
        prefix = 0
        count = 0
        
        for n in nums:
            prefix += n
            diff = prefix - k
            
            # If (prefix - k) exists as a prefix sum before,
            # it means there's a subarray ending here that sums to k.
            count += prefix_map[diff]
            
            # Update the frequency of the current prefix sum
            prefix_map[prefix] += 1
            
        return count
