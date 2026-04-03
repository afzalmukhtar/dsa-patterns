# 239. Sliding Window Maximum (Hard)

## Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

### Examples

**Example 1:**
- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output:** `[3,3,5,5,6,7]`
- **Explanation:** 
```text
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**
- **Input:** `nums = [1], k = 1`
- **Output:** `[1]`

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## 💡 Implementation Strategy

### Why the Naive Approach Fails
A simple $O(n \times k)$ approach using `max(window)` at each step will TLE (Time Limit Exceeded) for $n=10^5, k=10^5$. We need a way to find the maximum in $O(1)$ amortized time as we slide.

### Pattern: Monotonic Deque
We use a **Deque (Double-Ended Queue)** to store indices of elements in the current window. We maintain the deque such that:
1.  **Indices are in bounds:** The first element's index `q[0]` must be within `[i - k + 1, i]`.
2.  **Values are Monotonic:** Elements in the deque are stored in **decreasing order** of their values.

**The "Aha!" Insight:**
When a new element `nums[i]` arrives:
- Any element in the deque that is **smaller** than `nums[i]` can never be the maximum again (because `nums[i]` is larger and stays in the window longer). So, we pop them from the back.
- This keeps the largest element's index at the front of the deque.

### Complexity
- **Time:** $O(n)$ because each element is pushed and popped from the deque at most once.
- **Space:** $O(k)$ for the deque.

---

## Code

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque() # stores indices
        ans = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window bounds
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 2. Maintain monotonic decreasing order:
            # Remove indices whose values are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            dq.append(i)
            
            # 3. If window has reached size k, the front is the max
            if i >= k - 1:
                ans.append(nums[dq[0]])
                
        return ans
```
