# Pattern #1: Two Pointers

> **Status:** 🔄 In Progress | **Solved:** 16

---

## 1. What is it?
Imagine reading a book from both ends simultaneously — one finger at the first page, another at the last. They move toward each other based on what you find. **Two Pointers** is an optimization technique where you use two indices to traverse a data structure (usually an array or linked list) to find a pair, triplet, or subarray that meets a condition.

## 2. When do I use it?
Look for these signals:
- **Sorted Array:** Sum, pair, or triplet problems.
- **In-place Reorganization:** Moving zeros, removing duplicates, partitioning.
- **Strings:** Palindrome checks, reversing.
- **Trigger:** "Find two numbers in a sorted array that sum to X" or "Rearrange elements without extra space."

## 3. The Mental Model
Picture a sorted array. You want a pair that sums to a target.
```text
[ 1,  3,  5,  7,  9,  11 ]  Target: 10
  L                    R    1+11 = 12 (Too Big)
  L               R         1+9 = 10 (MATCH!)
```
Because it's sorted, moving `R` left *always* decreases the sum, and moving `L` right *always* increases it. You have a compass.

## 4. Brute Force First
Check every possible pair using nested loops.
```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target: return [i, j]
```
- **Time:** $O(n^2)$
- **Why it's slow:** It ignores the sorted order, checking pairs that are logically impossible based on previous results.

## 5. The Optimization Insight
The sorted order allows you to **eliminate** an entire row or column of possibilities with every single move. If `arr[L] + arr[R]` is too big, then `arr[R]` paired with *any* element after `L` will also be too big. So we can safely discard `R` and move inward.

## 6. The Optimal Solution
Use two pointers to converge on the answer in a single pass.
- **Time:** $O(n)$
- **Space:** $O(1)$

```python
def solve(arr, target):
    L, R = 0, len(arr) - 1
    while L < R:
        curr = arr[L] + arr[R]
        if curr == target: return [L, R]
        if curr < target: L += 1
        else: R -= 1
    return []
```

## 7. The Template
```python
def two_pointer_template(arr):
    L, R = 0, len(arr) - 1 # Opposite ends
    # OR L, R = 0, 1       # Same direction
    
    while L < R:
        if condition_met(arr[L], arr[R]):
            return result
        elif need_more:
            L += 1
        else:
            R -= 1
```

## 8. Variations and Edge Cases
- **Unsorted Array:** Sort it first ($O(n \log n)$) to use the pattern.
- **Duplicates:** Use `while` loops to skip identical values to avoid duplicate triplets.
- **3Sum:** Fix one element with a loop, then use Two Pointers for the remaining two.
- **Container Water:** Moving the shorter pointer is the only way to potentially find more water.

## 9. Practice Problems

| # | Problem | Difficulty | Sub-Pattern |
|---|---------|------------|-------------|
| 1 | [Two Sum II - Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Easy | Opposite Ends |
| 2 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Opposite Ends |
| 3 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Same Direction |
| 4 | [Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | Same Direction |
| 5 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | Fixed Element + 2P |
| 6 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Greedy Movement |
| 7 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Two Pointers / Precomputation |
| 11 | [Container With Most Water](./problems/11-container-with-most-water.md) ([Sol](./problems/11-container-with-most-water.py)) | TBD | Added from local |
| 125 | [Valid Palindrome](./problems/125-valid-palindrome.md) ([Sol](./problems/125-valid-palindrome.py)) | TBD | Added from local |
| 15 | [3Sum](./problems/15-3sum.md) ([Sol](./problems/15-3sum.py)) | TBD | Added from local |
| 16 | [3Sum Closest](./problems/16-3sum-closest.md) ([Sol](./problems/16-3sum-closest.py)) | TBD | Added from local |
| 167 | [Two Sum Ii Input Array Is Sorted](./problems/167-two-sum-ii-input-array-is-sorted.md) ([Sol](./problems/167-two-sum-ii-input-array-is-sorted.py)) | TBD | Added from local |
| 18 | [4Sum](./problems/18-4sum.md) ([Sol](./problems/18-4sum.py)) | TBD | Added from local |
| 19 | [Remove Nth Node From End Of List](./problems/19-remove-nth-node-from-end-of-list.md) ([Sol](./problems/19-remove-nth-node-from-end-of-list.py)) | TBD | Added from local |
| 26 | [Remove Duplicates From Sorted Array](./problems/26-remove-duplicates-from-sorted-array.md) ([Sol](./problems/26-remove-duplicates-from-sorted-array.py)) | TBD | Added from local |
| 27 | [Remove Element](./problems/27-remove-element.md) ([Sol](./problems/27-remove-element.py)) | TBD | Added from local |
| 283 | [Move Zeroes](./problems/283-move-zeroes.md) ([Sol](./problems/283-move-zeroes.py)) | TBD | Added from local |
| 344 | [Reverse String](./problems/344-reverse-string.md) ([Sol](./problems/344-reverse-string.py)) | TBD | Added from local |
| 345 | [Reverse Vowels Of A String](./problems/345-reverse-vowels-of-a-string.md) ([Sol](./problems/345-reverse-vowels-of-a-string.py)) | TBD | Added from local |
| 42 | [Trapping Rain Water](./problems/42-trapping-rain-water.md) ([Sol](./problems/42-trapping-rain-water.py)) | TBD | Added from local |
| 680 | [Valid Palindrome Ii](./problems/680-valid-palindrome-ii.md) ([Sol](./problems/680-valid-palindrome-ii.py)) | TBD | Added from local |
| 75 | [Sort Colors](./problems/75-sort-colors.md) ([Sol](./problems/75-sort-colors.py)) | TBD | Added from local |
| 80 | [Remove Duplicates From Sorted Array Ii](./problems/80-remove-duplicates-from-sorted-array-ii.md) ([Sol](./problems/80-remove-duplicates-from-sorted-array-ii.py)) | TBD | Added from local |
