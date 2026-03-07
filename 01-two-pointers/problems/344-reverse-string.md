# 344. Reverse String

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/reverse-string/)

---

## 📝 Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with $O(1)$ extra memory.

---

## 💡 Examples

**Example 1:**
- **Input:** `s = ["h","e","l","l","o"]`
- **Output:** `["o","l","l","e","h"]`

**Example 2:**
- **Input:** `s = ["H","a","n","n","a","h"]`
- **Output:** `["h","a","n","n","a","H"]`

---

## ⚙️ Constraints

- $1 \le s.length \le 10^5$
- `s[i]` is a printable ascii character.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is the most fundamental **Two-Pointer** problem.
2.  **In-Place Modification:** 
    -   To reverse an array without extra space, we swap elements from the ends and move towards the middle.
    -   `left` pointer starts at index `0`.
    -   `right` pointer starts at index `len(s) - 1`.
3.  **The Swap:**
    -   Swap `s[left]` and `s[right]`.
    -   Increment `left`, decrement `right`.
    -   Stop when `left >= right`.
4.  **Pythonic Tip:** Python allows simultaneous assignment `a, b = b, a`, making the swap very concise.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We visit each element once (specifically, we perform $n/2$ swaps).
- **Space Complexity:** $O(1)$ — We only use two integer pointers.
