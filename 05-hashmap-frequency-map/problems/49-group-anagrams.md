# 49. Group Anagrams

**Difficulty:** Medium

**Topics:** Array, Hash Table, String, Sorting

---

### Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples

**Example 1:**
- **Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`
- **Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

**Example 2:**
- **Input:** `strs = [""]`
- **Output:** `[[""]]`

**Example 3:**
- **Input:** `strs = ["a"]`
- **Output:** `[["a"]]`

### Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

### Brute Force Approach ($O(N^2 \cdot L \log L)$)

This approach uses a nested loop to compare every string with every other string. A `seen` set is used to track strings that have already been grouped to avoid duplicate processing.

```python
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:
        return [strs]
    res = []
    seen = set()
    for i in range(len(strs)):
        if i in seen: # Using index to handle duplicate strings
            continue
        seen.add(i)
        part = [strs[i]]
        key = sorted(strs[i])
        for j in range(i + 1, len(strs)):
            if key == sorted(strs[j]) and j not in seen:
                part.append(strs[j])
                seen.add(j)
        res.append(part)
    return res
```

### Hash Map Approach (Optimal)

The key insight is to find a "signature" that is identical for all anagrams (like a sorted string or a character frequency tuple) and use it as a key in a Hash Map ($O(1)$ lookup).

#### 1. Sorting Signature ($O(N \cdot L \log L)$)
Sort each string to create a unique key for its anagram group.

#### 2. Character Count Signature ($O(N \cdot L)$)
Use an array of size 26 to count character frequencies. A tuple of these counts serves as the Hash Map key. This is the most efficient for large inputs.
