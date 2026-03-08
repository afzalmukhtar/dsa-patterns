# 121. Best Time to Buy and Sell Stock

> **Difficulty:** Easy | **Link:** [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## 📝 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## 💡 Examples

**Example 1:**
- **Input:** `prices = [7,1,5,3,6,4]`
- **Output:** `5`
- **Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**
- **Input:** `prices = [7,6,4,3,1]`
- **Output:** `0`
- **Explanation:** In this case, no transactions are done and the max profit = 0.

---

## ⚙️ Constraints

- $1 \le prices.length \le 10^5$
- $0 \le prices[i] \le 10^4$

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a **Single-Pass Greedy Scan** (often categorized as a degenerate case of Sliding Window or Two Pointers). We want to find the largest difference between two numbers where the smaller number (buy) appears before the larger number (sell).
2.  **Brute Force:** Check every pair of days $(i, j)$ where $j > i$. This would take $O(n^2)$ time.
3.  **Optimal Approach (Greedy):**
    -   Keep track of the minimum price encountered so far (`last_min`).
    -   As we iterate through the prices, calculate the potential profit if we sold on the current day (`price - last_min`).
    -   Update the maximum profit if the current potential profit is greater.
    -   This ensures we are always "buying" at the lowest possible price seen before the current "sell" day.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the array once.
- **Space Complexity:** $O(1)$ — We only use two variables: `max_profit` and `last_min`.
