from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum in each sliding window of size k using a Monotonic Deque.
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        dq = deque()  # stores indices, where values at these indices are decreasing
        ans = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are no longer in the sliding window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 2. Maintain a monotonic decreasing deque:
            # While the current number is greater than the value at the back index,
            # those indices can never be the maximum again. Pop them.
            while dq and nums[dq[-1]] < num:
                dq.pop()
                
            dq.append(i)
            
            # 3. If we've processed at least k elements, the front of the deque
            # is the index of the maximum element for the current window.
            if i >= k - 1:
                ans.append(nums[dq[0]])
                
        return ans

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    expected1 = [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow(nums1, k1) == expected1, f"Test 1 Failed: {sol.maxSlidingWindow(nums1, k1)}"
    
    # Test 2
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    assert sol.maxSlidingWindow(nums2, k2) == expected2, f"Test 2 Failed: {sol.maxSlidingWindow(nums2, k2)}"
    
    # Test 3
    nums3 = [9, 11]
    k3 = 2
    expected3 = [11]
    assert sol.maxSlidingWindow(nums3, k3) == expected3, f"Test 3 Failed: {sol.maxSlidingWindow(nums3, k3)}"

    print("All tests passed!")
