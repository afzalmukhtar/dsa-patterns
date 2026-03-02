from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the running sum with the first k elements
        running_sum = max_sum = sum(nums[:k])
        
        # Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            # Update the sum by subtracting the element that is sliding out
            # and adding the element that is sliding in
            running_sum = running_sum - nums[i - k] + nums[i]
            # Update max_sum if the new running_sum is larger
            max_sum = max(max_sum, running_sum)

        # The maximum average is the maximum sum divided by k
        return max_sum / k
