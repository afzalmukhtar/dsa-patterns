# 53. Maximum Subarray (Medium)

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

### Examples

**Example 1:**
- **Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- **Output:** `6`
- **Explanation:** The subarray `[4,-1,2,1]` has the largest sum 6.

**Example 2:**
- **Input:** `nums = [1]`
- **Output:** `1`

**Example 3:**
- **Input:** `nums = [5,4,-1,7,8]`
- **Output:** `23`

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 💡 The "Aha!" Moment: Kadane's Algorithm

Kadane's algorithm is the most efficient way to solve the Maximum Subarray problem. It can be viewed through two lenses: **Dynamic Programming** and **Greedy**.

### The Core Logic
At every index `i`, you have a choice for the subarray ending at that position:
1. **Extend** the existing subarray (sum so far + `nums[i]`)
2. **Start fresh** with just `nums[i]`

**You choose whichever is larger.**

### Visual Illustration
Imagine you are walking through the array, carrying a "bag" of sum.
`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

1. At `-2`: Your bag is `[-2]`. Sum = -2.
2. At `1`: Should you add `1` to your bag of `-2` (total -1) or just throw away the old bag and start with `[1]`? **Start fresh with 1.**
3. At `-3`: Add `-3` to `1` (total -2) or start with `[-3]`? **Keep the bag (total -2)** because -2 > -3.
4. At `4`: Add `4` to `-2` (total 2) or start fresh with `[4]`? **Start fresh with 4.**
5. ... and so on.

### Where to use Kadane's? 🚨
- Finding the **maximum/minimum sum** of a contiguous subarray.
- Problems that can be reduced to the maximum subarray sum (e.g., "Maximum difference between two elements where the smaller comes first" can be turned into a subarray sum problem of differences).

### What to look out for? ⚠️
1. **All Negative Numbers:** If the array is `[-5, -1, -3]`, Kadane's should return `-1` (the largest single element). The implementation provided below handles this correctly by initializing with the first element.
2. **Empty Array:** Usually handled by constraints, but return `0` or an error if applicable.
3. **Empty Subarrays:** Some variations allow an empty subarray (sum = 0). If the max sum found is negative, you'd return 0 in that case.

---

## 🚀 Prefix Sum Connection
How does this relate to Prefix Sum?
`Sum(i, j) = Prefix[j] - Prefix[i-1]`
To maximize this, we want to subtract the **minimum possible prefix sum** we've seen so far from our current prefix sum.

```python
min_prefix = 0
max_sum = -float('inf')
current_prefix = 0
for x in nums:
    current_prefix += x
    max_sum = max(max_sum, current_prefix - min_prefix)
    min_prefix = min(min_prefix, current_prefix)
```
This is functionally equivalent to Kadane's!

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize with the first element
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # Decision: Extend the previous subarray or start a new one here?
            curr_sum = max(nums[i], curr_sum + nums[i])
            # Track the global maximum
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
```

**Complexity:**
- **Time:** $O(n)$ - one pass through the array.
- **Space:** $O(1)$ - only two variables needed.
