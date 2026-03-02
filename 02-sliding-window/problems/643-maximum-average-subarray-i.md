# 643. Maximum Average Subarray I

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)

---

## 📝 Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than $10^{-5}$ will be accepted.

---

## 💡 Examples

**Example 1:**
- **Input:** `nums = [1,12,-5,-6,50,3], k = 4`
- **Output:** `12.75000`
- **Explanation:** Maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`

**Example 2:**
- **Input:** `nums = [5], k = 1`
- **Output:** `5.00000`

---

## ⚙️ Constraints

- `n == nums.length`
- $1 \le k \le n \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** We need to find a contiguous subarray of a **fixed size** `k`. This is a classic **Fixed-Size Sliding Window** problem.
2.  **Brute Force:** Calculate the sum of every possible subarray of size `k`. This would take $O(n \cdot k)$ time.
3.  **Optimal Approach (Sliding Window):**
    -   Calculate the sum of the first `k` elements.
    -   Slide the window by one element at a time: subtract the element leaving the window and add the new element entering it.
    -   Keep track of the maximum sum encountered.
    -   The maximum average is simply `max_sum / k`.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the array once.
- **Space Complexity:** $O(1)$ — We only use a few variables for the sum.
