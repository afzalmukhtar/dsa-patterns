# 167. Two Sum II - Input Array Is Sorted

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

## 📝 Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where $1 \le index1 < index2 \le numbers.length$.

Return the indices of the two numbers, `index1` and `index2`, **each incremented by one**, as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You may **not** use the same element twice.

Your solution must use only **constant extra space**.

---

## 💡 Examples

**Example 1:**
- **Input:** `numbers = [2,7,11,15], target = 9`
- **Output:** `[1,2]`
- **Explanation:** The sum of 2 and 7 is 9. Therefore, `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

**Example 2:**
- **Input:** `numbers = [2,3,4], target = 6`
- **Output:** `[1,3]`
- **Explanation:** The sum of 2 and 4 is 6. Therefore `index1 = 1`, `index2 = 3`. We return `[1, 3]`.

**Example 3:**
- **Input:** `numbers = [-1,0], target = -1`
- **Output:** `[1,2]`
- **Explanation:** The sum of -1 and 0 is -1. Therefore `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

---

## ⚙️ Constraints

- $2 \le numbers.length \le 3 \cdot 10^4$
- $-1000 \le numbers[i] \le 1000$
- `numbers` is sorted in **non-decreasing order**.
- $-1000 \le target \le 1000$
- The tests are generated such that there is **exactly one solution**.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** Since the array is **sorted** and we need to find two elements that satisfy a condition (summing to target), the **Two Pointers** pattern is highly effective.
2.  **Brute Force:** Check all possible pairs $(i, j)$ where $i < j$. This would take $O(n^2)$ time.
3.  **Optimal Approach (Two Pointers):**
    -   Initialize two pointers: `left` at the beginning (0) and `right` at the end (`len(numbers) - 1`) of the array.
    -   Calculate the sum of the elements at these pointers: `sum_num = numbers[left] + numbers[right]`.
    -   If `sum_num == target`, we've found the solution. Return `[left + 1, right + 1]` (as it's 1-indexed).
    -   If `sum_num < target`, we need a larger sum. Since the array is sorted, we move the `left` pointer to the right (`left += 1`).
    -   If `sum_num > target`, we need a smaller sum. We move the `right` pointer to the left (`right -= 1`).
    -   Because there's exactly one solution, we are guaranteed to find it.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — We traverse the array at most once with the two pointers.
- **Space Complexity:** $O(1)$ — We only use two pointer variables, meeting the constant extra space requirement.
