# 345. Reverse Vowels of a String

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)

---

## 📝 Problem Statement

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

---

## 💡 Examples

**Example 1:**
- **Input:** `s = "IceCreAm"`
- **Output:** `"AceCreIm"`
- **Explanation:** The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, `s` becomes `"AceCreIm"`.

**Example 2:**
- **Input:** `s = "leetcode"`
- **Output:** `"leotcede"`

---

## ⚙️ Constraints

- $1 \le s.length \le 3 \times 10^5$
- `s` consists of printable ASCII characters.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a **Two-Pointer** problem where we only care about specific characters (vowels).
2.  **Strings are Immutable:** In Python, strings cannot be modified in-place. We must convert the string to a `list` of characters first.
3.  **Vowel Lookup:** 
    -   Create a set of vowels `{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}`.
    -   Using a **set** provides $O(1)$ average time complexity for lookups, which is faster than checking a list.
4.  **Two-Pointer Logic:**
    -   `left` pointer starts at `0`.
    -   `right` pointer starts at `len(s) - 1`.
    -   Skip non-vowel characters using `while` loops.
    -   When both pointers land on vowels, swap them and increment/decrement both pointers.
5.  **Reconstruct:** Join the list back into a string and return.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the string once.
- **Space Complexity:** $O(n)$ — We create a list of characters of size `n` to handle the immutability of strings in Python.
