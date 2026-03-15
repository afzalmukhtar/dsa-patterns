# 76. Minimum Window Substring

> **Difficulty:** Hard | **Link:** [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

---

## 📝 Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

---

## 💡 Examples

**Example 1:**
- **Input:** `s = "ADOBECODEBANC", t = "ABC"`
- **Output:** `"BANC"`
- **Explanation:** The minimum window substring `"BANC"` includes 'A', 'B', and 'C' from string `t`.

**Example 2:**
- **Input:** `s = "a", t = "a"`
- **Output:** `"a"`

**Example 3:**
- **Input:** `s = "a", t = "aa"`
- **Output:** `""`
- **Explanation:** Both 'a's from `t` must be included in the window. Since the largest window of `s` only has one 'a', return empty string.

---

## ⚙️ Constraints

- $m == s.length$
- $n == t.length$
- $1 \le m, n \le 10^5$
- `s` and `t` consist of uppercase and lowercase English letters.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is the "boss" level of **Variable-Size Sliding Window** problems. We need to find the *shortest* window that satisfies a complex frequency condition.
2.  **Window Strategy (Have vs Need):**
    -   Use a frequency map `count_t` for string `t`.
    -   `need` = number of **unique** characters in `t`.
    -   `have` = number of unique characters in the current window that meet the required frequency in `t`.
    -   Expand `R`: If `s[R]` is in `t` and its count in the window reaches its required count in `t`, increment `have`.
    -   While `have == need`:
        -   The window is valid. Update the `min_size` and record the substring.
        -   Shrink `L`: If `s[L]` is in `t` and its count drops below the required frequency, decrement `have`.
3.  **Optimization:** Instead of slicing the string `s[L:R+1]` every time (which is $O(m)$), store the `L` and `R` indices and slice once at the end.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(m + n)$ — $O(n)$ to build the map for `t`, and $O(m)$ to slide across `s`.
- **Space Complexity:** $O(k)$ — where $k$ is the number of unique characters in $s$ and $t$ (at most 52 for English letters).
