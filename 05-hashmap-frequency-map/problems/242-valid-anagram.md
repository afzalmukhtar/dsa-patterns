# 242. Valid Anagram

**Difficulty:** Easy

**Topics:** Hash Table, String, Sorting

---

### Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples

**Example 1:**
- **Input:** `s = "anagram"`, `t = "nagaram"`
- **Output:** `true`

**Example 2:**
- **Input:** `s = "rat"`, `t = "car"`
- **Output:** `false`

### Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Both the **Frequency Map** and **Sorting** approaches naturally adapt to Unicode because Python strings are Unicode-aware. However, one must consider **Unicode Normalization**. Some characters can be represented by different byte sequences (e.g., 'é' can be a single code point or 'e' + an accent code point). To handle this correctly, you should normalize both strings using `unicodedata.normalize('NFC', s)` before comparing.

---

### Frequency Map Approach (Recommended)

The most efficient way to check for an anagram is to count the frequency of each character in both strings. If the counts match, they are anagrams.

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```

- **Time Complexity:** $O(n)$ - where $n$ is the length of the strings.
- **Space Complexity:** $O(1)$ - since the character set is limited to 26 lowercase English letters (or $O(k)$ for Unicode, where $k$ is the number of unique characters).

### Sorting Approach

If two strings are anagrams, their sorted versions will be identical.

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

- **Time Complexity:** $O(n \log n)$ - due to the sorting operation.
- **Space Complexity:** $O(n)$ or $O(1)$ - depending on the language's implementation of `sorted()`.
