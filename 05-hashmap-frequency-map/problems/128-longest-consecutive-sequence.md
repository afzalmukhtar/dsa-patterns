# 128. Longest Consecutive Sequence (Medium)

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

**You must write an algorithm that runs in $O(n)$ time.**

### Examples

**Example 1:**
- **Input:** `nums = [100,4,200,1,3,2]`
- **Output:** `4`
- **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

**Example 2:**
- **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`
- **Output:** `9`

**Example 3:**
- **Input:** `nums = [1,0,1,2]`
- **Output:** `3`

### Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💡 Implementation Strategy

### Pattern: HashSet for $O(1)$ Lookup
The naive approach would be to sort the array and then find the longest sequence, but that would take $O(n \log n)$ time. To achieve $O(n)$, we use a HashSet.

1. **Store in Set:** Convert the input array into a set for $O(1)$ lookups.
2. **Identify Sequence Starts:** A number `n` is the start of a sequence if `n - 1` is NOT in the set.
3. **Count Sequence Length:** For each sequence start, increment a `target` value while `target` is in the set, and track the maximum length found.

### Complexity
- **Time:** $O(n)$. Although there is a `while` loop inside a `for` loop, each number is visited at most twice (once by the `for` loop and once by the `while` loop across all iterations).
- **Space:** $O(n)$ to store the numbers in a set.

---

## Code

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        set_nums = set(nums)
        max_seq = 0
        
        for n in set_nums:
            # Only start counting if 'n' is the beginning of a sequence
            if (n - 1) not in set_nums:
                target = n
                while target in set_nums:
                    target += 1
                
                max_seq = max(max_seq, target - n)
                
        return max_seq
```
