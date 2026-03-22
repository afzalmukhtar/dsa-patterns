from typing import List
from collections import Counter

class Solution:
    def topKFrequent_simple(self, nums: List[int], k: int) -> List[int]:
        """
        Simple Approach using Counter
        Time Complexity: O(N log N) - due to sorting in most_common()
        Space Complexity: O(N)
        """
        return [i[0] for i in Counter(nums).most_common(k)]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Heap Approach
        Time Complexity: O(N log k)
        Space Complexity: O(N + k)
        """
        import heapq
        count = Counter(nums)
        # min-heap to keep track of top k
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal Approach (Bucket Sort)
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Insight: The maximum frequency is len(nums). Create 'buckets' where 
        index is frequency and value is list of numbers with that frequency.
        """
        count = Counter(nums)
        # frequency -> [list of numbers]
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Iterate backwards from highest frequency bucket
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
