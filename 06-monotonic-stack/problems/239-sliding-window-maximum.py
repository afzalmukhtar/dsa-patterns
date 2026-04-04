from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        My understanding of the approach:
        1. We maintain a deque (monotonic queue) that stores indices of nums.
        2. As we traverse from start to end, we want to keep the largest elements 
           in the queue.
        3. If the incoming element nums[i] is larger than the elements at the 
           back of the queue, we pop them until the queue is empty or the back 
           element is larger. This maintains a decreasing order (monotonic) of values.
        4. We add the current index to the back of the queue.
        5. Before recording the maximum, we check if the element at the front 
           (the current maximum) is outside the current window of size k. 
           If the front index (queue[0]) is less than (i - k + 1), it's no longer 
           in range, so we popleft().
        6. Once the window reaches size k (i >= k - 1), we can start adding the 
           maximum (which is always at nums[queue[0]]) to our result list.
        """
        queue = deque([]) # monotonic queue, stores indices
        result = []

        for i in range(len(nums)):
            # Maintain monotonic property: remove smaller elements from back
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)

            # Check if current max is out of bounds (out of window range)
            if queue[0] < i - k + 1:
                queue.popleft()

            # Result is valid only after first window is complete (length k)
            if i >= k - 1:
                result.append(nums[queue[0]])
                
        return result
