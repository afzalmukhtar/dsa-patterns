# 238. Product of Array Except Self (Medium)

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

**You must write an algorithm that runs in $O(n)$ time and without using the division operation.**

### Examples

**Example 1:**
- **Input:** `nums = [1,2,3,4]`
- **Output:** `[24,12,8,6]`

**Example 2:**
- **Input:** `nums = [-1,1,0,-3,3]`
- **Output:** `[0,0,9,0,0]`

### Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

---

## 💡 Implementation Strategy

### Pattern: Prefix & Suffix Products
Since we cannot use division, we need another way to get the product of all elements except the current one. The key insight is that for any index `i`:
`answer[i] = (product of all elements to the left of i) * (product of all elements to the right of i)`

1. **Prefix Products:** We can iterate from left to right, maintaining a running product of all elements seen so far.
2. **Suffix Products:** We can iterate from right to left, maintaining a running product of all elements seen so far from the right.
3. **Space Optimization:** Instead of using two separate arrays for prefix and suffix products, we can use the output array to store prefix products first, and then multiply them by the suffix products on a second pass.

### Complexity
- **Time:** $O(n)$ where $n$ is the length of `nums`. We make two passes over the array.
- **Space:** $O(1)$ extra space if we don't count the output array.

---

## Code

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1]
        right = 1
        n = len(nums)
        for i in range(1, n):
            left.append(left[i - 1] * nums[i - 1])

        for i in range(n - 1, -1, -1):
            left[i] *= right
            right *= nums[i]

        return left
```
