# 75. Sort Colors

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Sorting

---

### Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

### Examples

**Example 1:**
- **Input:** `nums = [2,0,2,1,1,0]`
- **Output:** `[0,0,1,1,2,2]`

**Example 2:**
- **Input:** `nums = [2,0,1]`
- **Output:** `[0,1,2]`

### Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

---

### Dutch National Flag Algorithm (Three-Way Partition)

This problem is solved using three pointers to partition the array into three sections:
1. `[0, L-1]`: Elements equal to 0 (Red)
2. `[L, M-1]`: Elements equal to 1 (White)
3. `[R+1, n-1]`: Elements equal to 2 (Blue)

```python
def sortColors(nums: List[int]) -> None:
    L, M = 0, 0
    R = len(nums) - 1

    while M <= R:
        if nums[M] == 0:
            nums[L], nums[M] = nums[M], nums[L]
            L += 1
            M += 1
        elif nums[M] == 1:
            M += 1
        else: # nums[M] == 2
            nums[M], nums[R] = nums[R], nums[M]
            R -= 1
```

- **Time Complexity:** $O(n)$ - Single pass through the array.
- **Space Complexity:** $O(1)$ - Constant extra space used for pointers.

**Key Insight:** When swapping with the Right pointer (`R`), we do not increment the Middle pointer (`M`) because the element swapped from the end has not been processed yet and could be a 0, 1, or 2.
