# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy

**Topics:** Array, Two Pointers

---

### Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements.

Consider the number of unique elements in `nums` to be `k`. To get accepted, you need to do the following:
1. Modify the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were initially present in `nums`.
2. Return `k`.

### Examples

**Example 1:**
- **Input:** `nums = [1,1,2]`
- **Output:** `2, nums = [1,2,_]`

**Example 2:**
- **Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`
- **Output:** `5, nums = [0,1,2,3,4,_,_,_,_,_]`

### Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

---

### General Template for "At Most K" Duplicates

This template is useful for handling variations where each element can appear at most $K$ times (e.g., $K=1$ for unique elements, $K=2$ for at most two of each).

```python
def removeDuplicates(nums, k):
    # k = count allowed minus 1 (e.g., k=0 for unique elements)
    if not nums:
        return 0
        
    L = 0
    for R in range(1, len(nums)):
        # If we haven't reached the allowed count (L < k)
        # Or current element is different from the element at index L-k
        if L < k or nums[R] != nums[L - k]:
            L += 1
            nums[L] = nums[R]
            
    return L + 1
```

- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$
