# Pattern #4: Binary Search

> **Status:** 🔄 In Progress | **Solved:** 0

---

## 1. What is it?
Imagine you're searching for a word in a 1,000-page physical dictionary. You don't start at page 1. You open it in the middle, see if the word is before or after, and **discard half** the remaining pages with every flip. **Binary Search** is an $O(\log n)$ search algorithm that works on sorted arrays by repeatedly halving the search space.

## 2. When do I use it?
Look for these signals:
- **Sorted Data:** Arrays, lists, or sequences in increasing or decreasing order.
- **Sorted Range:** Finding a square root or an optimal value in a range.
- **Trigger:** "Find a number in a sorted array" or "Search for the first/last occurrence."

## 3. The Mental Model
Picture a sorted array. You start at the middle.
```text
Target: 7
Arr: [ 1,  3,  5,  7,  9,  11 ]
       L     M           R    (M=5, 5 < 7 -> search Right)
                L  M     R    (M=7, MATCH!)
```
Each step, the search range is cut in half. $O(\log n)$ means searching 1,000,000 items takes only ~20 steps!

## 4. Brute Force First
Search one-by-one (Linear Search).
```python
for i in range(len(arr)):
    if arr[i] == target: return i
```
- **Time:** $O(n)$
- **Why it's slow:** It ignores the sorted order, checking items it *already knows* are either too small or too big.

## 5. The Optimization Insight
Because the array is sorted, comparing the middle element with the target tells you **exactly** where the target *must* be. This information is powerful enough to ignore half the array every single time.

## 6. The Optimal Solution
Use `left` and `right` pointers to maintain the search space.
- **Time:** $O(\log n)$
- **Space:** $O(1)$

```python
def solve(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = L + (R - L) // 2 # Prevent overflow
        if arr[mid] == target: return mid
        if arr[mid] < target: L = mid + 1
        else: R = mid - 1
    return -1
```

## 7. The Template (Standard & Search Range)
```python
def binary_search_template(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if condition(arr[mid]):
            # Record or return
            pass
        if go_right(arr[mid]):
            L = mid + 1
        else:
            R = mid - 1
```

## 8. Variations and Edge Cases
- **Duplicate Elements:** Search for the "first" or "last" occurrence by continuing the search even after finding the target.
- **Searching on a Answer Range:** Use Binary Search to find the minimum possible "maximum work" (e.g., Koko Eating Bananas).
- **Rotated Sorted Array:** Determine which half (left or right) is "normally" sorted before deciding where to search.
- **Empty Array:** Always handle the base case.

## 9. Practice Problems

| # | Problem | Difficulty | Sub-Pattern |
|---|---------|------------|-------------|
| 1 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Core Pattern |
| 2 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Modified Range |
| 3 | [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Bound Search |
| 4 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Search on Answer |
| 5 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Advanced Partition |
