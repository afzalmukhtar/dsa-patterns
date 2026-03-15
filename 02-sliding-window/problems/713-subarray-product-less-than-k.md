# 713. Subarray Product Less Than K

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is **strictly less than** `k`.

---

## 💡 Examples

**Example 1:**
- **Input:** `nums = [10,5,2,6], k = 100`
- **Output:** `8`
- **Explanation:** The 8 subarrays that have product less than 100 are:
  `[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]`
  Note that `[10, 5, 2]` is not included as the product of 100 is not strictly less than `k`.

**Example 2:**
- **Input:** `nums = [1,2,3], k = 0`
- **Output:** `0`

---

## ⚙️ Constraints

- $1 \le nums.length \le 3 \cdot 10^4$
- $1 \le nums[i] \le 1000$
- $0 \le k \le 10^6$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This problem asks for the *number* of contiguous subarrays satisfying a product condition. This is a **Variable-Size Sliding Window** problem.
2.  **Window Strategy:**
    -   Maintain a running `product` of the elements in the window `[L, R]`.
    -   Expand the window using the right pointer `R`.
    -   If the `product` becomes $\ge k$, shrink the window from the left (`L`) until `product < k`.
    -   **Key Counting Insight:** For every valid window `[L, R]`, the number of new valid subarrays ending at `R` is exactly `R - L + 1`. 
        -   *Example:* In `[5, 2, 6]`, the subarrays ending at `6` are `[6]`, `[2, 6]`, and `[5, 2, 6]`. All of these are valid if the largest one is valid.
3.  **Edge Case:** If $k \le 1$, no subarray can have a product strictly less than $k$ (since all elements are $\ge 1$). Return `0` immediately.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Each element is added to the product once and removed at most once.
- **Space Complexity:** $O(1)$ — Only a few variables are used to track the window and product.
