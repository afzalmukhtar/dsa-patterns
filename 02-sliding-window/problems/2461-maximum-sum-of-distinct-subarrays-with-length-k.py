from typing import List
from collections import Counter

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Maximum sum of a subarray of length k with all distinct elements.
        
        Strategy: Use a fixed sliding window + Counter to track frequencies.
        Distinctness check: If len(counter) == k, all elements in window are distinct.
        
        Complexity:
        - Time: O(N) because we visit each element once.
        - Space: O(K) to store elements in the counter.
        """
        n = len(nums)
        if k > n:
            return 0
            
        count = Counter(nums[:k])
        window_sum = sum(nums[:k])
        
        # Initial window check
        max_sum = window_sum if len(count) == k else 0
        
        for i in range(k, n):
            # 1. Update window sum
            window_sum += nums[i] - nums[i - k]
            
            # 2. Update frequency map (Incoming)
            count[nums[i]] += 1
            
            # 3. Update frequency map (Outgoing)
            count[nums[i - k]] -= 1
            if count[nums[i - k]] == 0:
                del count[nums[i - k]]
            
            # 4. Check for distinct elements (size == k)
            if len(count) == k:
                max_sum = max(max_sum, window_sum)
        
        return max_sum
