from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Count subarrays of size k with average >= threshold using a fixed sliding window.
        
        Insight: 
        Average >= threshold  =>  sum / k >= threshold  =>  sum >= k * threshold
        Using the total sum required avoids floating-point division errors and is slightly faster.

        Time: O(N) since we visit each element once.
        Space: O(1) for running sum and counter.
        """
        window_sum = sum(arr[:k])
        sum_required = k * threshold
        count = 1 if window_sum >= sum_required else 0

        for i in range(k, len(arr)):
            # Slide the window: add incoming, remove outgoing
            window_sum += arr[i] - arr[i - k]
            if window_sum >= sum_required:
                count += 1

        return count
