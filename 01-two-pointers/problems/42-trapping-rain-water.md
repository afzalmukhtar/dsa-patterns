# 42. Trapping Rain Water

> **Difficulty:** Hard | **Link:** [LeetCode](https://leetcode.com/problems/trapping-rain-water/)

---

## 📝 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---

## 💡 Examples

**Example 1:**
- **Input:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- **Output:** `6`
- **Explanation:** The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of rain water (blue section) are being trapped.

**Example 2:**
- **Input:** `height = [4,2,0,3,2,5]`
- **Output:** `9`

---

## ⚙️ Constraints

- `n == height.length`
- $1 \le n \le 2 \cdot 10^4$
- $0 \le height[i] \le 10^5$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This problem can be solved using **Two Pointers (Opposite Ends)**. The amount of water trapped at any position depends on the minimum of the maximum height to its left and the maximum height to its right.
2.  **Core Logic:** 
    -   We use two pointers, `L` and `R`, starting at the ends of the array.
    -   We also maintain `maxL` (max height seen from the left) and `maxR` (max height seen from the right).
    -   If `maxL < maxR`, it means the bottleneck is on the left side. The water trapped at `L` is determined by `maxL`. We move `L` inward.
    -   If `maxR <= maxL`, the bottleneck is on the right side. The water trapped at `R` is determined by `maxR`. We move `R` inward.
3.  **Why it works:** By always moving the pointer with the smaller "max" wall, we ensure that the other side is guaranteed to have a wall at least as high, satisfying the `min(maxL, maxR)` requirement for trapping water.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Single pass through the array.
- **Space Complexity:** $O(1)$ — Only a few variables used for pointers and max heights.
