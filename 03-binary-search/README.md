# 03 — Binary Search

> **Status:** 🔄 In Progress | **Problems Solved:** 0

---

## 📌 Pattern Notes

### 1. What Is It?
Binary Search is a way to find something by repeatedly cutting your search space in half.

Instead of checking every possibility one by one ($O(n)$), you ask:
*"Is the answer in the left half or the right half?"*

Then throw away the half that can't contain the answer. Repeat until done.

**Key requirement:** The search space must be **monotonic** — meaning it's sorted, or there's a clear rule that lets you say "go left" or "go right."

### 2. When Do I Use It? — The Signals 🚨

| Clue in the problem | Why it points to Binary Search |
|---|---|
| "sorted array" | Classic. Search space is pre-organized |
| "find minimum/maximum that satisfies condition X" | Binary search on the answer |
| "return the index of..." | Searching for a position |
| $O(\log n)$ expected | Dead giveaway |
| "can we do X with capacity/speed/days = K?" | Binary search on a value range |
| The search space has a yes/no boundary | Split at the boundary |

### 3. The Mental Model
Imagine you're guessing a number between 1 and 100. Your friend says "higher" or "lower."

You don't start at 1. You guess 50 first. Half gone. Then 75 or 25. Half gone again. You find it in ~7 guesses instead of 100.

That's binary search. The "higher/lower" feedback is your condition that tells you which half to keep.

```text
Search space: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                              ^
                             mid
                "too small" → throw away left half
                "too big"   → throw away right half
```

### 4. Brute Force First
**Problem:** Find target 7 in `[1, 3, 5, 7, 9, 11]`
Naive approach: Check every element.
- Check 1 → no
- Check 3 → no
- Check 5 → no
- Check 7 → yes! ✓

$O(n)$ — fine for small arrays, terrible for 10 million elements.

### 5. The Optimization Insight — The "Aha" Moment 💡
The array is sorted. That means if `arr[mid] < target`, then everything to the left of `mid` is also too small. You can throw away the entire left half in one move.

You're not just skipping one element — you're skipping half the remaining search space every single step.
That's why it's $O(\log n)$: `n=1,000,000` → only ~20 comparisons needed.

### 6. The Optimal Solution — Step by Step
**Problem:** Find index of target 7 in `[1, 3, 5, 7, 9, 11]`

```text
arr = [1,  3,  5,  7,  9,  11]
idx =  0   1   2   3   4   5

Step 1:
  L=0, R=5, mid=2 → arr[2]=5 < 7 → go RIGHT
  [1,  3,  5, | 7,  9,  11]
              L              R

Step 2:
  L=3, R=5, mid=4 → arr[4]=9 > 7 → go LEFT
  [7,  9,  11]
   L   ^   R

Step 3:
  L=3, R=3, mid=3 → arr[3]=7 == 7 → FOUND ✓
```

### 7. The Template — Two Versions You Must Know

#### Version 1: Exact Match (find a value)
```python
def binary_search(arr, target):
    L, R = 0, len(arr) - 1
    
    while L <= R:
        mid = L + (R - L) // 2  # avoids integer overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            L = mid + 1   # target is in right half
        else:
            R = mid - 1   # target is in left half
    
    return -1  # not found
```

#### Version 2: Find the Boundary (the powerful one)
This is for problems like *"find the leftmost position where condition is True"*.
The idea: the search space looks like this:
```text
[False, False, False, True, True, True]
                      ^
                 find this boundary
```
```python
def find_left_boundary(arr):
    L, R = 0, len(arr) - 1
    result = -1
    
    while L <= R:
        mid = L + (R - L) // 2
        
        if condition(arr[mid]):   # True → might be our answer, but go LEFT for earlier one
            result = mid
            R = mid - 1
        else:                     # False → go RIGHT
            L = mid + 1
    
    return result
```
**The key mental shift:** Instead of stopping when you find *a* match, you **record it and keep searching** for a better (earlier/later) one.

### 8. Variations and Edge Cases

- **When array is rotated:** `[4, 5, 6, 7, 0, 1, 2]` ← rotated sorted array. One half is always sorted. Check which half, then decide where to go.
- **When there are duplicates:** `[1, 1, 1, 2, 3]` — `mid` might equal target but not be the leftmost one. Use boundary template instead of exact match.
- **Negative numbers / zeros:** Binary search doesn't care about the values — only that the space is monotonic. Works fine.
- **When searching on a VALUE RANGE (not an array!):**
  This is the most powerful and underrated form: *"A ship can carry weights 1–500 tons. What's the minimum capacity to ship all packages in D days?"*
  There's no array here — but the answer space (1 to 500) is sorted! Binary search on the answer directly.
  ```python
  L, R = min_possible_answer, max_possible_answer

  while L <= R:
      mid = (L + R) // 2
      if can_achieve(mid):   # is mid a valid answer?
          result = mid
          R = mid - 1        # try smaller
      else:
          L = mid + 1        # need bigger
  ```

---

## 🕵️ Deep Dive: The Loop Patterns and Complex Variations

> **❓ Common Doubt:** *"How do I solve the medium and hard problems? I didn't understand the concept of searching on an answer space or rotated arrays. Also, what is the difference between `while L <= R`, `while L < R`, and `while L + 1 < R`?"*

### Part 1: The Three Loop Patterns — Deeply Explained
This trips up everyone. Let's see exactly when each one breaks and why.

#### Pattern A: `while L <= R`
**Use when:** You're looking for an **exact match** and want to return immediately when found.
The loop runs while the window has at least 1 element. When `L > R`, the window is empty.
```text
arr = [1, 3, 5, 7, 9] (target = 10)
Step 1: L=0, R=4, mid=2 → arr[2]=5 < 10
Step 2: L=3, R=4, mid=3 → arr[3]=7 < 10  
Step 3: L=4, R=4, mid=4 → arr[4]=9 < 10
Step 4: L=5, R=4 → L > R, loop ends → return -1
```
*What breaks if you use L < R here?*
At Step 3: `L=4, R=4` → L is NOT < R → loop ends early! You never check the last element. Bug. 🐛

#### Pattern B: `while L < R`
**Use when:** You're **converging to a boundary** — you don't need an exact match, you're finding a position.
The loop ends when `L == R`. At that point, both pointers are pointing at the same answer.
```text
arr = [F, F, F, T, T, T]   ← find first True
       0  1  2  3  4  5

Step 1: L=0, R=5, mid=2 → False → go right → L=3
Step 2: L=3, R=5, mid=4 → True  → record, go left → R=4
Step 3: L=3, R=4, mid=3 → True  → record, go left → R=3
Step 4: L=3, R=3 → L==R → STOP. Answer is index 3 ✓
```
*Notice: you never need `L == R` check inside the loop because when they meet, you already have your answer.*

#### Pattern C: `while L + 1 < R`
**Use when:** Your mid calculation could cause an **infinite loop** because L and R are adjacent and mid always equals L.
This happens when you write `R = mid` and `L = mid`.
`L=3, R=4` → `mid = (3+4)//2 = 3 = L`. If you do `L = mid` → `L=3` again. Infinite loop! 🔄
Pattern C stops before they're adjacent, leaving you with exactly 2 candidates to check manually after the loop.

**The Cheat Sheet:**
- Searching for EXACT VALUE? → `L <= R`
- Converging to a BOUNDARY (first/last true)? → `L < R`
- Risk of INFINITE LOOP (using `mid` without +/- 1)? → `L + 1 < R`

---

### Part 2: Sqrt(x) — Binary Search on Answer Space
**Problem:** Given integer `n`, find `floor(√n)` without using `sqrt()`.
Example: `n = 8` → answer is `2` (because √8 = 2.82..., floor = 2)

**The insight:** You're not searching an array. You're searching the **answer space**: integers from `0` to `n`.
*"If I guess that √n = mid, how do I know if mid is too big, too small, or just right?"*
- `mid * mid == n` → exact answer
- `mid * mid < n` → mid might be the floor, but try bigger
- `mid * mid > n` → mid is too big, go smaller

```text
L=1, R=8
Step 1: mid=4 → 4*4=16 > 8 → too big → R=3
Step 2: L=1, R=3, mid=2 → 2*2=4 < 8 → possible! record=2 → L=3
Step 3: L=3, R=3, mid=3 → 3*3=9 > 8 → too big → R=2
Step 4: L=3 > R=2 → loop ends
Return record = 2 ✓
```
```python
def mySqrt(n):
    if n < 2: return n
    L, R, result = 1, n, 0
    while L <= R:
        mid = L + (R - L) // 2
        if mid * mid == n: return mid              
        elif mid * mid < n: result = mid; L = mid + 1             
        else: R = mid - 1             
    return result
```

---

### Part 3: Find Minimum in Rotated Array
**Problem:** `[4, 5, 6, 7, 0, 1, 2]` — Originally sorted, then rotated. Find the minimum.

**The key insight:** A rotated array always has **one sorted half and one unsorted half**.
At any `mid`, you compare `arr[mid]` with `arr[R]`:
- If `arr[mid] > arr[R]`: mid is in the LEFT (bigger) half. Minimum MUST be in the right half. → `L = mid + 1`
- If `arr[mid] < arr[R]`: mid is in the RIGHT (smaller) half. Minimum is at mid or to its LEFT. → `R = mid`

```python
def findMin(arr):
    L, R = 0, len(arr) - 1
    while L < R:              # Pattern B: converging to boundary
        mid = L + (R - L) // 2
        if arr[mid] > arr[R]: L = mid + 1       
        else: R = mid           
    return arr[L]             # L == R, that's our answer
```

---

### Part 4: Koko Eating Bananas
**Problem:** Piles of bananas `[3, 6, 7, 11]`. Guards return in `H=8` hours. She eats at speed `K` bananas/hour. What's the minimum `K` to finish all piles in `H` hours?

**The "aha" moment:** *"Minimum K that satisfies a condition"* — that phrase is the trigger. The search space isn't an array — it's all possible speeds from `1` to `max(piles)`.
*"If I pick a speed K, can I immediately check if it works?"* Yes!
```text
K=1: takes forever → ✗
...
K=3: takes long    → ✗
K=4: works!        → ✓  ← find this boundary
K=5: works!        → ✓
```
This is exactly the boundary template!
```python
import math
def minEatingSpeed(piles, H):
    L, R = 1, max(piles)
    result = max(piles)
    while L <= R:
        mid = L + (R - L) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= H:        # this speed works!
            result = mid      # record it, try slower
            R = mid - 1
        else:
            L = mid + 1       # too slow, need faster
    return result
```

---

### Part 5: Median of Two Sorted Arrays (Hard)
**The trigger:** $O(\log n)$ in the constraints + two sorted arrays = binary search on a partition.
**The core idea:** Binary search on **where to cut nums1**. Once you know the cut in `nums1`, the cut in `nums2` is forced (to keep equal halves). Then check if the partition is valid (is `max(left) ≤ min(right)`?).

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

> **💡 Practice Strategy:** Here is your complete, curated Binary Search problem list — organized by the exact sub-patterns we covered, in the order you should practice them.

### 🟢 STAGE 1 — Classic Binary Search (Pattern A: L <= R)
*Master the fundamentals. Exact match, find index, find value.*

| # | Problem | Why it's here |
|---|---------|---------------|
| 1 | [Binary Search](https://leetcode.com/problems/binary-search/) | The purest form. Do this first, no excuses. |
| 2 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Exact match OR find where it would go |
| 3 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | Classic "higher/lower" feedback loop |
| 4 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Binary search on a value range, not an array |
| 5 | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Apply binary search row by row |

### 🟢 STAGE 2 — Boundary / First & Last Occurrence (Pattern B: L < R)
*Stop at exact match → Start recording & keep searching.*

| # | Problem | Why it's here |
|---|---------|---------------|
| 6 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Textbook `[F,F,F,T,T,T]` → find first `T` |
| 7 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Find left boundary AND right boundary separately |
| 8 | [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | Boundary search with wrap-around edge case |
| 9 | [Arranging Coins](https://leetcode.com/problems/arranging-coins/) | Find last "valid" row — boundary on answer space |
| 10 | [H-Index II](https://leetcode.com/problems/h-index-ii/) | Boundary search on a sorted citations array |

### 🟡 STAGE 3 — Binary Search on Answer Space (The powerful one)
*No sorted array exists. You CREATE the search space from min→max possible answer.*

| # | Problem | Search Space | Condition to check |
|---|---------|--------------|--------------------|
| 11 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Speed `1` → `max(piles)` | Can she finish in H hours? |
| 12 | [Capacity to Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | `max(weight)` → `sum(weights)` | Can ship finish in D days? |
| 13 | [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | `1` → `max(nums)` | Is sum of divisions ≤ threshold? |
| 14 | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | `1` → `max(bloomDay)` | Can we make m bouquets? |
| 15 | [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) | `1` → `10^7` | Can you arrive within hour limit? |

### 🟡 STAGE 4 — Rotated Sorted Array (Tricky conditions)
*The array is sorted but someone rotated it. One half is always sorted — figure out which.*

| # | Problem | The trick |
|---|---------|-----------|
| 16 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Compare `arr[mid]` with `arr[R]` to find unsorted half |
| 17 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Find which half is sorted, then decide where target lives |
| 18 | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Same but with duplicates — adds an extra `L++` edge case |
| 19 | [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Rotated + duplicates combined |

### 🟡 STAGE 5 — Peak Finding
*The array goes up then down. Binary search still works because you can always tell which side the peak is on.*

| # | Problem | Why |
|---|---------|-----|
| 20 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | Warm up — single peak, simple |
| 21 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Multiple peaks, find any one — classic $O(\log n)$ |

### 🔴 STAGE 6 — Hard / Multi-dimensional
*Only after Stage 1–5 feel comfortable.*

| # | Problem | Why it's hard |
|---|---------|---------------|
| 22 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Treat 2D matrix as 1D sorted array — index math needed |
| 23 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Binary search on value range + count how many ≤ mid |
| 24 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Binary search on answer space, condition is complex |
| 25 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary search on partition — hardest of the pattern |

---

*Notes and problems will be added here over time.*