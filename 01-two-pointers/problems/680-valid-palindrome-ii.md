# 680. Valid Palindrome II

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)

---

## 📝 Problem Statement

Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

---

## 💡 Examples

**Example 1:**
- **Input:** `s = "aba"`
- **Output:** `true`

**Example 2:**
- **Input:** `s = "abca"`
- **Output:** `true`
- **Explanation:** You could delete the character 'c'.

**Example 3:**
- **Input:** `s = "abc"`
- **Output:** `false`

---

## ⚙️ Constraints

- $1 \le s.length \le 10^5$
- `s` consists of lowercase English letters.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a variation of the **Two-Pointer** palindrome check.
2.  **The "One Deletion" Rule:** 
    -   Standard palindrome check uses `left` and `right` pointers. 
    -   If `s[left] == s[right]`, we simply move inward.
    -   If `s[left] != s[right]`, we have two choices to see if a palindrome is still possible:
        1.  Skip the left character (`left + 1`) and check if the remaining substring `s[left+1...right]` is a palindrome.
        2.  Skip the right character (`right - 1`) and check if the remaining substring `s[left...right-1]` is a palindrome.
3.  **Efficiency:** We only perform the "skip" check once. This keeps the time complexity linear.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the string once. In the worst case (one mismatch), we check two substrings, but each is still $O(n)$.
- **Space Complexity:** $O(1)$ — We use pointers and a helper function that doesn't use extra space (if we avoid string slicing).
