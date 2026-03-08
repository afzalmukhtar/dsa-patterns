# 287. Find the Duplicate Number

**Difficulty:** Medium

**Topics:** Array, Two Pointers (Fast & Slow), Binary Search, Bit Manipulation

---

### Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and using only constant extra space.

### Examples

**Example 1:**
- **Input:** `nums = [1,3,4,2,2]`
- **Output:** `2`

**Example 2:**
- **Input:** `nums = [3,1,3,4,2]`
- **Output:** `3`

**Example 3:**
- **Input:** `nums = [3,3,3,3,3]`
- **Output:** `3`

### Constraints
- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

### Follow up
- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

---

### Fast and Slow Pointers (Floyd's Cycle-Finding)

The problem can be mapped to a linked list cycle detection problem. Each number `nums[i]` is treated as a pointer to the index `nums[i]`. Because there's a duplicate number, at least two indices point to the same value, creating a cycle.

1. **Phase 1: Finding the Intersection Point**
   - Start `slow` at `nums[0]` and `fast` at `nums[nums[0]]`.
   - Move `slow` by one step (`slow = nums[slow]`) and `fast` by two steps (`fast = nums[nums[fast]]`) until they meet.
2. **Phase 2: Finding the Entrance to the Cycle**
   - Reset `slow` to 0.
   - Move both `slow` and `fast` by one step until they meet again.
   - The meeting point is the duplicate number.

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the meeting point of slow and fast
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the entrance to the cycle (the duplicate)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

- **Time Complexity:** $O(n)$ - Linear scan of the cycle.
- **Space Complexity:** $O(1)$ - Constant extra space as required.
