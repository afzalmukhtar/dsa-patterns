# 209. Minimum Size Subarray Sum

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

## 📝 Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

---

## 💡 Examples

**Example 1:**
- **Input:** `target = 7, nums = [2,3,1,2,4,3]`
- **Output:** `2`
- **Explanation:** The subarray `[4,3]` has the minimal length under the problem constraint.

**Example 2:**
- **Input:** `target = 4, nums = [1,4,4]`
- **Output:** `1`

**Example 3:**
- **Input:** `target = 11, nums = [1,1,1,1,1,1,1,1]`
- **Output:** `0`

---

## ⚙️ Constraints

- $1 \le target \le 10^9$
- $1 \le nums.length \le 10^5$
- $1 \le nums[i] \le 10^4$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This problem asks for a subarray meeting a certain condition (sum $\ge$ target), which is a classic indicator for the **Sliding Window** technique. Specifically, this is a **Variable-Size Sliding Window**.
2.  **Window Strategy:**
    -   Expand the window by moving the right pointer (`R`) and adding `nums[R]` to the `window_sum`.
    -   While the `window_sum` is $\ge$ `target`, we've found a valid subarray.
    -   Try to shrink the window from the left (`L`) to find the *minimal* length that still satisfies the condition.
    -   Update the `min_size` during each valid window.
3.  **Edge Case:** If no such subarray is found, return `0`.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Each element is visited at most twice (once by the right pointer and once by the left pointer).
- **Space Complexity:** $O(1)$ — We only use a few variables for the pointers, sum, and minimum length.
