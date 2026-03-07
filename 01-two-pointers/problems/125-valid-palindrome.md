# 125. Valid Palindrome

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/valid-palindrome/)

---

## 📝 Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. **Alphanumeric characters include letters and numbers.**

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## 💡 Examples

**Example 1:**
- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** `"amanaplanacanalpanama"` is a palindrome.

**Example 2:**
- **Input:** `s = "race a car"`
- **Output:** `false`
- **Explanation:** `"raceacar"` is not a palindrome.

**Example 3:**
- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** `s` is an empty string `""` after removing non-alphanumeric characters.

---

## ⚙️ Constraints

- $1 \le s.length \le 2 \times 10^5$
- `s` consists only of printable ASCII characters.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a classic **Two-Pointer** problem where we compare characters from both ends moving towards the center.
2.  **Filter Alphanumeric Characters:**
    -   The problem explicitly states that "alphanumeric" includes both letters AND numbers.
    -   In Python, we use the `.isalnum()` method to check this. Using `.isalpha()` would incorrectly skip numbers.
3.  **Handle Case Sensitivity:** Convert all characters to lowercase using `.lower()` before comparing.
4.  **In-Place Comparison:** 
    -   Instead of creating a new filtered string (which uses $O(n)$ space), we can use two pointers (`left` and `right`) to skip non-alphanumeric characters on the fly.
5.  **Termination:** The loop continues as long as `left < right`.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the string at most once.
- **Space Complexity:** $O(1)$ — We only use two pointers and no extra data structures.
