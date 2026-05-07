# 🔍 Pattern: Binary Search

> **Status:** 🔄 In Progress | **Solved:** 5

---

## 1. What Is It?
Binary Search is a way to find something by repeatedly cutting your search space in half. Instead of checking every possibility one by one ($O(n)$), you ask: **"Is the answer in the left half or the right half?"**, then throw away the half that can't contain the answer.

**Key requirement:** The search space must be **monotonic** — meaning it's sorted, or there's a clear rule that lets you say "go left" or "go right."

## 2. When Do I Use It? — The Signals
| Signal | Why it points to Binary Search |
| :--- | :--- |
| **"Sorted array"** | Classic. Search space is pre-organized. |
| **"Find min/max that satisfies condition X"** | Binary search on the answer space. |
| **"Return the index of..."** | Searching for a specific position. |
| **$O(\log n)$ expected** | Dead giveaway for binary search. |
| **"Search space has a yes/no boundary"** | Splitting at the boundary point. |
| 1351 | [Count Negative Numbers In A Sorted Matrix](./problems/1351-count-negative-numbers-in-a-sorted-matrix.md) ([Sol](./problems/1351-count-negative-numbers-in-a-sorted-matrix.py)) | TBD | Added from local |
| 35 | [Search Insert Position](./problems/35-search-insert-position.md) ([Sol](./problems/35-search-insert-position.py)) | TBD | Added from local |
| 374 | [Guess Number Higher Or Lower](./problems/374-guess-number-higher-or-lower.md) ([Sol](./problems/374-guess-number-higher-or-lower.py)) | TBD | Added from local |
| 69 | [Sqrtx](./problems/69-sqrtx.md) ([Sol](./problems/69-sqrtx.py)) | TBD | Added from local |
| 704 | [Binary Search](./problems/704-binary-search.md) ([Sol](./problems/704-binary-search.py)) | TBD | Added from local |

## 3. The Mental Model
Imagine guessing a number between 1 and 100. Your friend says "higher" or "lower." You don't start at 1; you guess 50. If they say "higher," you've eliminated 50 numbers in one move.

```text
Search space: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                              ^
                             mid
                "too small" → throw away left half
                "too big"   → throw away right half
```

## 4. Brute Force First
Checking every element sequentially (Linear Search).
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: return i
    return -1
```
- **Time Complexity:** $O(n)$
- **Constraint:** Terrible for large datasets (e.g., 10 million elements).

## 5. The Optimization Insight — The "Aha!" Moment
If the array is sorted, comparing `arr[mid]` to the `target` doesn't just eliminate one element—it eliminates **half the remaining search space**.
- **Time Complexity:** $O(\log n)$
- **Scale:** $n = 1,000,000 \rightarrow$ only ~20 comparisons needed.

## 6. The Three Loop Patterns (Crucial)
Choosing the right loop condition and pointer update is where most bugs happen.

### Pattern A: `while L <= R`
- **Use when:** Searching for an **exact match**.
- **Termination:** $L > R$ (window is empty).
- **Pointer Update:** `L = mid + 1`, `R = mid - 1`.

### Pattern B: `while L < R`
- **Use when:** Converging to a **boundary** (e.g., first "True" in `[F, F, T, T]`).
- **Termination:** $L == R$. Both pointers meet at the answer.
- **Pointer Update:** `L = mid + 1`, `R = mid`.

### Pattern C: `while L + 1 < R`
- **Use when:** `mid` calculation could cause an **infinite loop** (L and R are adjacent).
- **Termination:** $L$ and $R$ are adjacent. Check both manually after the loop.
- **Pointer Update:** `L = mid`, `R = mid`.

## 7. The Templates

### Version 1: Exact Match
```python
def binary_search(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = L + (R - L) // 2 # Avoids integer overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1
```

### Version 2: Find the Boundary (The Powerful One)
Used for: "find the leftmost position where condition is True".
```python
def find_left_boundary(arr):
    L, R = 0, len(arr) - 1
    result = -1
    while L <= R:
        mid = L + (R - L) // 2
        if condition(arr[mid]): # True -> record and go LEFT for earlier one
            result = mid
            R = mid - 1
        else:                   # False -> go RIGHT
            L = mid + 1
    return result
```

## 8. Variations and Edge Cases
- **Sqrt(x):** Binary search on the answer space `0 → x`. Condition: `mid * mid <= x`.
- **Rotated Array:** One half is always sorted. Compare `arr[mid]` with `arr[R]` to find the pivot.
- **Search on Answer Range:** No array exists, but the result space (e.g., eating speeds 1-100) is monotonic. Use the boundary template.

---

## 🧭 Practice Roadmap

### 🟢 Stage 1: Classic Binary Search (`L <= R`)
1. [Binary Search (LC 704)](https://leetcode.com/problems/binary-search/)
2. [Search Insert Position (LC 35)](https://leetcode.com/problems/search-insert-position/)
3. [Guess Number Higher or Lower (LC 374)](https://leetcode.com/problems/guess-number-higher-or-lower/)
4. [Sqrt(x) (LC 69)](https://leetcode.com/problems/sqrtx/)
5. [Count Negative Numbers in Sorted Matrix (LC 1351)](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

### 🟢 Stage 2: Boundary / First & Last Occurrence (`L < R`)
6. [First Bad Version (LC 278)](https://leetcode.com/problems/first-bad-version/)
7. [Find First and Last Position (LC 34)](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
8. [Smallest Letter Greater Than Target (LC 744)](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
9. [Arranging Coins (LC 441)](https://leetcode.com/problems/arranging-coins/)
10. [H-Index II (LC 275)](https://leetcode.com/problems/h-index-ii/)

### 🟡 Stage 3: Binary Search on Answer Space
11. [Koko Eating Bananas (LC 875)](https://leetcode.com/problems/koko-eating-bananas/)
12. [Capacity to Ship Packages Within D Days (LC 1011)](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
13. [Smallest Divisor Given a Threshold (LC 1283)](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)
14. [Minimum Days to Make m Bouquets (LC 1482)](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
15. [Minimum Speed to Arrive on Time (LC 1870)](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)

### 🟡 Stage 4: Rotated Sorted Array
16. [Find Minimum in Rotated Sorted Array (LC 153)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
17. [Search in Rotated Sorted Array (LC 33)](https://leetcode.com/problems/search-in-rotated-sorted-array/)
18. [Search in Rotated Sorted Array II (LC 81)](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
19. [Find Minimum in Rotated Sorted Array II (LC 154)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

### 🟡 Stage 5: Peak Finding
20. [Peak Index in a Mountain Array (LC 852)](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
21. [Find Peak Element (LC 162)](https://leetcode.com/problems/find-peak-element/)

### 🔴 Stage 6: Hard / Multi-dimensional
22. [Search a 2D Matrix (LC 74)](https://leetcode.com/problems/search-a-2d-matrix/)
23. [Kth Smallest Element in a Sorted Matrix (LC 378)](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
24. [Split Array Largest Sum (LC 410)](https://leetcode.com/problems/split-array-largest-sum/)
25. [Median of Two Sorted Arrays (LC 4)](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---
*Built with curiosity, designed for mastery. 🚀*
