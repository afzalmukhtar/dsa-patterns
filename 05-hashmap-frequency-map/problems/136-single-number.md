# 136. Single Number

**Difficulty:** Easy

**Topics:** Array, Hash Table, Bit Manipulation

---

### Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only **constant extra space**.

### Examples

**Example 1:**
- **Input:** `nums = [2,2,1]`
- **Output:** `1`

**Example 2:**
- **Input:** `nums = [4,1,2,1,2]`
- **Output:** `4`

**Example 3:**
- **Input:** `nums = [1]`
- **Output:** `1`

### Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

---

### Frequency Map Approach

This approach uses a hash map to count occurrences. While it achieves $O(n)$ time, it requires $O(n)$ space, which technically violates the problem's **constant space** constraint.

```python
from collections import Counter

def singleNumber(nums: List[int]) -> int:
    counts = Counter(nums)
    for num, count in counts.items():
        if count == 1:
            return num
```

- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

### Bit Manipulation Approach (Optimal)

The most efficient solution uses the **XOR** operator. 
- $a \oplus 0 = a$
- $a \oplus a = 0$
- $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$

By XORing all numbers in the array, all pairs will cancel each other out, leaving only the single number.

```python
def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res
```

- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$
