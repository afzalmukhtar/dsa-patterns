# Pattern #2: Sliding Window

> **Status:** 🔄 In Progress | **Solved:** 15

---

## 1. What is it?
Imagine looking through a physical window at a long wall of numbers. The window has a size (fixed or flexible), and you **slide** it from left to right — never jumping back. At every position, you add the new element coming in and remove the old element going out.

## 2. When do I use it?
Look for these signals:
- **Subarray / Substring:** Problems involving contiguous elements.
- **Maximum / Minimum:** "Find the max sum of any subarray of size k."
- **K Distinct / K Elements:** "Shortest subarray with at most k distinct characters."
- **Trigger:** "Find the longest/shortest substring that satisfies a condition."

## 3. The Mental Model
Think of a train moving through stations.
```text
Window (size 3): [2, 1, 5] 1, 3, 2  (sum = 8)
Slide Right:      2 [1, 5, 1] 3, 2  (sum = 7)
```
Instead of recomputing the whole sum (1+5+1), you just do: `8 - 2 (out) + 1 (in) = 7`. This is O(1) per step instead of O(k).

## 4. Brute Force First
Try every possible window and sum its contents.
```python
for i in range(len(arr) - k + 1):
    current_sum = sum(arr[i : i + k]) # O(k) work
```
- **Time:** $O(n \times k)$
- **Why it's slow:** You're recomputing the overlapping part (the middle of the window) over and over.

## 5. The Optimization Insight
When you move the window one step:
- Only **one** element leaves the window.
- Only **one** element enters the window.
Everything else in the middle stays exactly the same. We only update the state with the `in` and `out` elements.

## 6. The Optimal Solution
Use a single pass to update the window state in $O(1)$.
- **Time:** $O(n)$
- **Space:** $O(1)$ (or $O(k)$ for frequency maps)

```python
def solve(arr, k):
    win_sum = sum(arr[:k])
    best = win_sum
    for i in range(k, len(arr)):
        win_sum += arr[i] - arr[i-k]
        best = max(best, win_sum)
    return best
```

## 7. The Template (Variable Window)
```python
def sliding_window_template(arr):
    L = 0
    state = {}
    best = 0
    for R in range(len(arr)):
        # 1. Expand: Add R to state
        add(state, arr[R])
        
        # 2. Shrink: While invalid, move L
        while invalid(state):
            remove(state, arr[L])
            L += 1
            
        # 3. Update Answer
        best = max(best, R - L + 1)
    return best
```

## 8. Variations and Edge Cases
- **Fixed Size:** Simple `in/out` logic.
- **Variable Size:** Use `while` to shrink L until the condition is met.
- **Shortest vs Longest:**
  - *Longest:* Record answer **after** the `while` loop.
  - *Shortest:* Record answer **inside** the `while` loop (right when it becomes valid).
- **Frequency Maps:** Use when tracking "distinct characters" or "target counts."

## 9. Practice Problems

| # | Problem | Difficulty | Window Type |
|---|---------|------------|-------------|
| 1 | [Max Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Fixed |
| 2 | [Longest Substring No Repeats](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Variable (Max) |
| 3 | [Min Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | Variable (Min) |
| 4 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | Variable (Max) |
| 5 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed (Freq Map) |
| 6 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Variable (Min/Target) |
