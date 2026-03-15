# 1004. Max Consecutive Ones III

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## 📝 Problem Statement

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

---

## 💡 Examples

**Example 1:**
- **Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`
- **Output:** `6`
- **Explanation:** `[1,1,1,0,0,1,1,1,1,1,1]`. Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

**Example 2:**
- **Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3`
- **Output:** `10`
- **Explanation:** `[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]`. Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

---

## ⚙️ Constraints

- $1 \le nums.length \le 10^5$
- `nums[i]` is either `0` or `1`.
- $0 \le k \le nums.length$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a **Variable-Size Sliding Window** problem. We need to find the longest subarray (window) that contains at most `k` zeros.
2.  **Window Strategy:**
    -   Expand the window using the right pointer `R`.
    -   If we encounter a `0`, increment a `zero_count`.
    -   If `zero_count > k`, the window is invalid. Shrink it from the left (`L`) until `zero_count` is back within the limit `k`.
    -   The maximum size of any valid window is our answer.
3.  **Key Insight:** Instead of "flipping" zeros, we simply "permit" up to `k` zeros within our window.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Each element is processed by the right pointer once and the left pointer at most once.
- **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for variables.
