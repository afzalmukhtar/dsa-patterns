# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium

**Topics:** Array, Two Pointers

---

### Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with $O(1)$ extra memory.

### Examples

**Example 1:**
- **Input:** `nums = [1,1,1,2,2,3]`
- **Output:** `5, nums = [1,1,2,2,3,_]`
- **Explanation:** Your function should return `k = 5`, with the first five elements of `nums` being 1, 1, 2, 2 and 3 respectively.

**Example 2:**
- **Input:** `nums = [0,0,1,1,1,1,2,3,3]`
- **Output:** `7, nums = [0,0,1,1,2,3,3,_,_]`
- **Explanation:** Your function should return `k = 7`, with the first seven elements of `nums` being 0, 0, 1, 1, 2, 3 and 3 respectively.

### Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

---

### General Solution (Two Pointers)

This problem is a specific case of the "At Most K" duplicates pattern. By setting the allowed duplicates parameter to 1 (meaning 2 occurrences total), we can use a single template to solve both this problem and its "Easy" predecessor (LeetCode 26).

```python
def removeDuplicates(nums: List[int]) -> int:
    L = 0
    k = 1 # Allows k + 1 occurrences (k=1 for at most 2)

    for R in range(1, len(nums)):
        # Check if we can place the current element:
        # 1. We haven't filled k+1 slots yet (L < k)
        # 2. The element at R is different from the element k slots back
        if L < k or nums[R] != nums[L - k]:
            L += 1
            nums[L] = nums[R]
            
    return L + 1
```

- **Time Complexity:** $O(n)$ - We traverse the array once.
- **Space Complexity:** $O(1)$ - Modification is done in-place.
