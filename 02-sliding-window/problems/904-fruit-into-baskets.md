# 904. Fruit Into Baskets

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/fruit-into-baskets/)

---

## 📝 Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the $i^{th}$ tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

1.  You only have **two baskets**, and each basket can only hold a **single type of fruit**. There is no limit on the amount of fruit each basket can hold.
2.  Starting from any tree of your choice, you must pick **exactly one fruit from every tree** (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
3.  Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the *maximum* number of fruits you can pick.

---

## 💡 Examples

**Example 1:**
- **Input:** `fruits = [1,2,1]`
- **Output:** `3`
- **Explanation:** We can pick from all 3 trees.

**Example 2:**
- **Input:** `fruits = [0,1,2,2]`
- **Output:** `3`
- **Explanation:** We can pick from trees `[1,2,2]`. If we had started at the first tree, we would only pick from trees `[0,1]`.

**Example 3:**
- **Input:** `fruits = [1,2,3,2,2]`
- **Output:** `4`
- **Explanation:** We can pick from trees `[2,3,2,2]`. If we had started at the first tree, we would only pick from trees `[1,2]`.

---

## ⚙️ Constraints

- $1 \le fruits.length \le 10^5$
- $0 \le fruits[i] < fruits.length$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** Despite the "baskets" and "farm" analogy, this problem is equivalent to: **"Find the longest contiguous subarray that contains at most 2 distinct integers."** This is a classic **Variable-Size Sliding Window** problem.
2.  **Window Strategy:**
    -   Maintain a frequency map (like a `Counter` or `dict`) to track the types of fruits and their counts in the current window `[L, R]`.
    -   Expand the window using the right pointer `R`.
    -   If the number of distinct fruit types (size of the map) exceeds 2, shrink the window from the left (`L`).
    -   When shrinking, decrement the count of the fruit at `L`. If its count reaches 0, remove it from the map entirely.
3.  **Optimization:** Since we only need to track 2 types, a simple dictionary is very efficient ($O(1)$ space since the map size is capped at 3).

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Each tree is visited by the right pointer once and the left pointer at most once.
- **Space Complexity:** $O(1)$ — The frequency map will store at most 3 fruit types at any given time.
