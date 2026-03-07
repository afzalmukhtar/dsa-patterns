# 16. 3Sum Closest

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/3sum-closest/)

---

## 📝 Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the **sum** of the three integers.

You may assume that each input would have exactly one solution.

---

## 💡 Examples

**Example 1:**
- **Input:** `nums = [-1,2,1,-4], target = 1`
- **Output:** `2`
- **Explanation:** The sum that is closest to the target is `2`. `(-1 + 2 + 1 = 2)`.

**Example 2:**
- **Input:** `nums = [0,0,0], target = 1`
- **Output:** `0`
- **Explanation:** The sum that is closest to the target is `0`. `(0 + 0 + 0 = 0)`.

---

## ⚙️ Constraints

- $3 \le nums.length \le 500$
- $-1000 \le nums[i] \le 1000$
- $-10^4 \le target \le 10^4$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is almost identical to **3Sum**. Since we need to find a combination of numbers near a target, and the array can be sorted, the **Two Pointers** "Converging" technique is the optimal way to avoid $O(n^3)$ brute force.
2.  **The "Pin and Squeeze" Strategy:**
    -   **Sort** the array first (essential for the pointers to work).
    -   **Pin** one number by iterating through the array (`i`).
    -   **Squeeze** the remaining space using two pointers: `left` (at `i + 1`) and `right` (at the end).
3.  **The Decision Rule:**
    -   Calculate `current_sum = nums[i] + nums[left] + nums[right]`.
    -   If `current_sum == target`, we found the perfect match. Return it immediately.
    -   If `current_sum < target`, we need a larger number to get closer to the target $ightarrow$ move `left` inward.
    -   If `current_sum > target`, we need a smaller number to get closer to the target $ightarrow$ move `right` inward.
4.  **Tracking the Winner:** At every step, check if the distance (`abs(current_sum - target)`) is smaller than our previously recorded `closest_sum`.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n^2)$ — One loop to fix the first number, and a nested two-pointer scan for each fixed number.
- **Space Complexity:** $O(1)$ to $O(n)$ — Depends on the sorting algorithm's space complexity.
