# 06 — Monotonic Stack & Deque

> **Status:** 🔄 In Progress | **Problems Solved:** 1

---

## 📌 Pattern Notes

### 1. What is it?
A Monotonic Stack (or Deque) is a data structure where elements are always stored in a specific order (either **strictly increasing** or **strictly decreasing**).

When a new element arrives that would break the order, you "pop" elements from the stack until the order can be maintained.

### 2. When to use it? (signals) 🚨
- **Next Greater/Smaller Element:** "Find the first element to the right that is larger than the current one."
- **Nearest Smaller Element:** "Find the first element to the left that is smaller."
- **Sliding Window Maximum:** "Find the max in every window of size $k$."
- **Online range queries:** When you need to maintain a maximum/minimum in a moving range.

---

## 🗂️ Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | [Sliding Window Maximum](./problems/239-sliding-window-maximum.md) | Hard | Monotonic Deque (decreasing) to track the max in $O(1)$. |

---

*Notes and problems will be added here over time.*
