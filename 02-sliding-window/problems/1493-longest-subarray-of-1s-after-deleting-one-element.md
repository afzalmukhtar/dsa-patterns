# 1493. Longest Subarray of 1's After Deleting One Element

> **Difficulty:** Medium | **Link:** [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

---

## 📝 Problem Statement

Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only `1`'s in the resulting array. Return `0` if there is no such subarray.

---

## 💡 Examples

**Example 1:**
- **Input:** `nums = [1,1,0,1]`
- **Output:** `3`
- **Explanation:** After deleting the number at index 2 (the 0), `[1,1,1]` contains 3 ones.

**Example 2:**
- **Input:** `nums = [0,1,1,1,0,1,1,0,1]`
- **Output:** `5`
- **Explanation:** After deleting the zero at index 4, `[0,1,1,1,1,1,0,1]` has a longest subarray of 5 ones.

**Example 3:**
- **Input:** `nums = [1,1,1]`
- **Output:** `2`
- **Explanation:** You **must** delete one element, so the result is 2 ones.

---

## ⚙️ Constraints

- $1 \le nums.length \le 10^5$
- `nums[i]` is either `0` or `1`.

---

## 🧠 Thought Process

1.  **Identify the Pattern:** This is a **Variable-Size Sliding Window** problem. We want to find the longest window that contains at most one `0`.
2.  **Window Strategy:**
    -   Expand the window using the right pointer `R`.
    -   Keep track of the count of zeros (`count`) inside the window.
    -   If `count > 1`, shrink the window from the left (`L`) until `count` is back to 1.
    -   The window size is always `R - L + 1`. Since we *must* delete one element (even if it's a 1), the final answer for any window is `(R - L + 1) - 1`, which simplifies to `R - L`.
3.  **Edge Case:** If the array contains only ones, we still must delete one, resulting in `length - 1`.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(n)$ — Each element is visited at most twice.
- **Space Complexity:** $O(1)$ — We only use variables for the pointers and the zero count.
