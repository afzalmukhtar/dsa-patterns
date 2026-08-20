# 🧠 DSA Master Recap: Everything Learned & Implemented

Welcome to your comprehensive master recap. This document summarizes all **69 implemented problems**, core mental models, code templates, edge-case invariants, and exact code links across the **10 active DSA patterns** in this repository.

---

## 📊 High-Level Progress Dashboard

| Pattern | Status | Implemented Problems | Key Focus Areas |
| :--- | :---: | :---: | :--- |
| **01. Two Pointers** | 🔄 Covered | **16** | Opposite-end convergence, fast-slow same-direction, 3Sum/4Sum, Dutch National Flag |
| **02. Sliding Window** | 🔄 Covered | **15** | Fixed-size windows, dynamic shrinking/expanding, frequency hashing, exact matches |
| **03. Binary Search** | 🔄 Covered | **5** | Discrete boundary search, predicate functions, search insert, monotonic spaces |
| **04. Fast & Slow Pointers** | 🔄 Covered | **4** | Floyd's Cycle Detection (Tortoise & Hare), cycle start math, linked list midpoints |
| **05. Prefix Sum** | 🔄 Covered | **1** | $O(1)$ range queries, prefix & suffix running products without division |
| **06. HashMap / Frequency Map** | 🔄 Covered | **8** | $O(1)$ complement lookups, anagram signatures, bucket sort for Top-K, prefix-sum hashing |
| **07. Monotonic Stack** | 🔄 Covered | **6** | Next/Previous Greater/Smaller elements, histogram area rectangles, sliding window maximum |
| **08. BFS / Level Order** | 🔄 Covered | **9** | Queue FIFO, level-by-level traversal, shortest path in unweighted graphs, multi-source BFS |
| **09. DFS / Backtracking** | 🔄 Covered | **4** | Tree recursion, height & diameter calculation, bottom-up tree aggregation, path sums |
| **10. Dynamic Programming** | 🔄 Covered | **1** | Kadane's algorithm, optimal substructure, 1D local vs. global maximums |
| **11-16. Next Patterns** | ⏳ Queued | *Ready* | Greedy, Intervals, Heaps/Priority Queues, Graph Patterns, Tries, Bit Manipulation |

**Total Solutions Implemented:** **69 Problems** (Markdown Explanations + Python Solutions)
**Curated Roadmaps:** [🎯 Blind 75 Mapping](file:///home/afzal/projects/dsa-patterns/dsa-patterns/practice/blind75.md) | [🎯 NeetCode 150 Mapping](file:///home/afzal/projects/dsa-patterns/dsa-patterns/practice/neetcode150.md)

---

## 🎯 Quick Pattern Recognition Matrix

| If the problem asks for... | And the data has... | Primary Pattern |
| :--- | :--- | :--- |
| Pair/triplet sum, palindrome, partitioning | Sorted array or in-place reorganization | **Two Pointers** |
| Subarray / substring optimal length or sum | Contiguous sequence, running constraint | **Sliding Window** |
| Cycle detection or linked list middle | Linked list or cyclic array index mapping | **Fast & Slow Pointers** |
| Target search, exact boundary, min/max answer | Monotonic property, sorted sequence | **Binary Search** |
| Instant range sum query, running sub-products | Cumulative operations, no element division | **Prefix Sum** |
| Exact pair matching, frequency counts, grouping | Unsorted data, $O(1)$ complement lookup | **HashMap / Set** |
| Nearest greater/smaller element, rectangle heights | Unresolved lookback/lookahead elements | **Monotonic Stack** |
| Shortest step count, level-by-level tree view | Unweighted graph, grid expansion | **BFS (Level-Order / Multi-Source)** |
| Exhaustive paths, tree structure/depth/diameter | Tree traversal, permutation / combinations | **DFS / Backtracking** |
| Optimal subproblem overlap, largest subarray | Subproblems depend on previous states | **Dynamic Programming** |

---

## 01. Two Pointers

### 💡 Mental Model & Intuition
Think of two runners on a track. They either:
1. **Convergently walk toward each other** (`L` at start, `R` at end): Ideal when sorted order allows eliminating an entire half-space on each decision.
2. **Move in the same direction at different speeds** (`slow` writes valid data, `fast` scans): Ideal for in-place filtering and deduplication.

```text
Opposite Ends (Sorted):
[ 1,   3,   5,   7,   9,   11 ]   Target = 10
  L                         R     -> 1 + 11 = 12 (> 10, decrement R)
  L                    R          -> 1 + 9  = 10 (MATCH!)
```

### 🛠️ Standard Template
```python
def two_pointers_opposite(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        curr = nums[L] + nums[R]
        if curr == target:
            return [L, R]
        elif curr < target:
            L += 1
        else:
            R -= 1
    return []
```

### 📚 Implemented Problems (16)
1. **Container With Most Water (LC 11)**: [`11-container-with-most-water.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/11-container-with-most-water.md) | [`11-container-with-most-water.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/11-container-with-most-water.py)
2. **Valid Palindrome (LC 125)**: [`125-valid-palindrome.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/125-valid-palindrome.md) | [`125-valid-palindrome.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/125-valid-palindrome.py)
3. **3Sum (LC 15)**: [`15-3sum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/15-3sum.md) | [`15-3sum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/15-3sum.py)
4. **3Sum Closest (LC 16)**: [`16-3sum-closest.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/16-3sum-closest.md) | [`16-3sum-closest.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/16-3sum-closest.py)
5. **Two Sum II - Input Array Is Sorted (LC 167)**: [`167-two-sum-ii-input-array-is-sorted.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/167-two-sum-ii-input-array-is-sorted.md) | [`167-two-sum-ii-input-array-is-sorted.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/167-two-sum-ii-input-array-is-sorted.py)
6. **4Sum (LC 18)**: [`18-4sum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/18-4sum.md) | [`18-4sum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/18-4sum.md)
7. **Remove Nth Node From End of List (LC 19)**: [`19-remove-nth-node-from-end-of-list.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/19-remove-nth-node-from-end-of-list.md) | [`19-remove-nth-node-from-end-of-list.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/19-remove-nth-node-from-end-of-list.py)
8. **Remove Duplicates from Sorted Array (LC 26)**: [`26-remove-duplicates-from-sorted-array.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/26-remove-duplicates-from-sorted-array.md) | [`26-remove-duplicates-from-sorted-array.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/26-remove-duplicates-from-sorted-array.py)
9. **Remove Element (LC 27)**: [`27-remove-element.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/27-remove-element.md) | [`27-remove-element.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/27-remove-element.py)
10. **Move Zeroes (LC 283)**: [`283-move-zeroes.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/283-move-zeroes.md) | [`283-move-zeroes.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/283-move-zeroes.py)
11. **Reverse String (LC 344)**: [`344-reverse-string.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/344-reverse-string.md) | [`344-reverse-string.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/344-reverse-string.py)
12. **Reverse Vowels of a String (LC 345)**: [`345-reverse-vowels-of-a-string.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/345-reverse-vowels-of-a-string.md) | [`345-reverse-vowels-of-a-string.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/345-reverse-vowels-of-a-string.py)
13. **Trapping Rain Water (LC 42)**: [`42-trapping-rain-water.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/42-trapping-rain-water.md) | [`42-trapping-rain-water.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/42-trapping-rain-water.py)
14. **Valid Palindrome II (LC 680)**: [`680-valid-palindrome-ii.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/680-valid-palindrome-ii.md) | [`680-valid-palindrome-ii.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/680-valid-palindrome-ii.py)
15. **Sort Colors (LC 75)**: [`75-sort-colors.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/75-sort-colors.md) | [`75-sort-colors.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/75-sort-colors.py)
16. **Remove Duplicates from Sorted Array II (LC 80)**: [`80-remove-duplicates-from-sorted-array-ii.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/80-remove-duplicates-from-sorted-array-ii.md) | [`80-remove-duplicates-from-sorted-array-ii.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/01-two-pointers/problems/80-remove-duplicates-from-sorted-array-ii.py)

---

## 02. Sliding Window

### 💡 Mental Model & Intuition
A camera lens sliding over contiguous elements. 
- **Fixed Window (size $k$):** Expand to size $k$, then slide by adding `nums[R]` and subtracting `nums[L]`.
- **Variable Window:** Expand `R` until constraint is violated; then shrink `L` until valid again.

```text
Variable Window: Longest Substring Without Repeating Characters
"a  b  c  a  b  c  b  b"
[a  b  c]                len = 3
   [b  c  a]             len = 3 (shifted L past duplicate 'a')
```

### 🛠️ Standard Template
```python
def dynamic_sliding_window(s):
    L = 0
    state = {}
    best = 0
    for R in range(len(s)):
        # 1. Expand: include s[R] into state
        state[s[R]] = state.get(s[R], 0) + 1
        
        # 2. Shrink: while window is invalid, evict s[L]
        while invalid_condition(state):
            state[s[L]] -= 1
            L += 1
            
        # 3. Update answer
        best = max(best, R - L + 1)
    return best
```

### 📚 Implemented Problems (15)
1. **Max Consecutive Ones III (LC 1004)**: [`1004-max-consecutive-ones-iii.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1004-max-consecutive-ones-iii.md) | [`1004-max-consecutive-ones-iii.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1004-max-consecutive-ones-iii.py)
2. **Best Time to Buy and Sell Stock (LC 121)**: [`121-best-time-to-buy-and-sell-stock.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/121-best-time-to-buy-and-sell-stock.md) | [`121-best-time-to-buy-and-sell-stock.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/121-best-time-to-buy-and-sell-stock.py)
3. **Number of Sub-arrays of Size K and Avg >= Threshold (LC 1343)**: [`1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.md) | [`1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py)
4. **Maximum Number of Vowels in Substring of Length K (LC 1456)**: [`1456-maximum-number-of-vowels-in-a-substring-of-given-length.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1456-maximum-number-of-vowels-in-a-substring-of-given-length.md) | [`1456-maximum-number-of-vowels-in-a-substring-of-given-length.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1456-maximum-number-of-vowels-in-a-substring-of-given-length.py)
5. **Longest Subarray of 1's After Deleting One Element (LC 1493)**: [`1493-longest-subarray-of-1s-after-deleting-one-element.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1493-longest-subarray-of-1s-after-deleting-one-element.md) | [`1493-longest-subarray-of-1s-after-deleting-one-element.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1493-longest-subarray-of-1s-after-deleting-one-element.py)
6. **Substrings of Size Three with Distinct Characters (LC 1876)**: [`1876-substrings-of-size-three-with-distinct-characters.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1876-substrings-of-size-three-with-distinct-characters.md) | [`1876-substrings-of-size-three-with-distinct-characters.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/1876-substrings-of-size-three-with-distinct-characters.md)
7. **Minimum Size Subarray Sum (LC 209)**: [`209-minimum-size-subarray-sum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/209-minimum-size-subarray-sum.md) | [`209-minimum-size-subarray-sum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/209-minimum-size-subarray-sum.py)
8. **Maximum Sum of Distinct Subarrays With Length K (LC 2461)**: [`2461-maximum-sum-of-distinct-subarrays-with-length-k.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/2461-maximum-sum-of-distinct-subarrays-with-length-k.md) | [`2461-maximum-sum-of-distinct-subarrays-with-length-k.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/2461-maximum-sum-of-distinct-subarrays-with-length-k.py)
9. **Longest Substring Without Repeating Characters (LC 3)**: [`3-longest-substring-without-repeating-characters.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/3-longest-substring-without-repeating-characters.md) | [`3-longest-substring-without-repeating-characters.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/3-longest-substring-without-repeating-characters.py)
10. **Find All Anagrams in a String (LC 438)**: [`438-find-all-anagrams-in-a-string.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/438-find-all-anagrams-in-a-string.md) | [`438-find-all-anagrams-in-a-string.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/438-find-all-anagrams-in-a-string.py)
11. **Permutation in String (LC 567)**: [`567-permutation-in-string.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/567-permutation-in-string.md) | [`567-permutation-in-string.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/567-permutation-in-string.py)
12. **Maximum Average Subarray I (LC 643)**: [`643-maximum-average-subarray-i.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/643-maximum-average-subarray-i.md) | [`643-maximum-average-subarray-i.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/643-maximum-average-subarray-i.py)
13. **Subarray Product Less Than K (LC 713)**: [`713-subarray-product-less-than-k.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/713-subarray-product-less-than-k.md) | [`713-subarray-product-less-than-k.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/713-subarray-product-less-than-k.py)
14. **Minimum Window Substring (LC 76)**: [`76-minimum-window-substring.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/76-minimum-window-substring.md) | [`76-minimum-window-substring.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/76-minimum-window-substring.py)
15. **Fruit Into Baskets (LC 904)**: [`904-fruit-into-baskets.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/904-fruit-into-baskets.md) | [`904-fruit-into-baskets.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/02-sliding-window/problems/904-fruit-into-baskets.py)

---

## 03. Binary Search

### 💡 Mental Model & Intuition
Halving search space in $O(\log n)$. Not just for sorted arrays, but **any search space that has a monotonic Boolean predicate** $P(x)$ (i.e., `[False, False, ..., True, True]`).

```text
Search Space: [ 1, 3, 5, 7, 9, 11 ] Target = 7
L = 0, R = 5, mid = 2 (val = 5) < 7 -> Discard left half, L = mid + 1 = 3
L = 3, R = 5, mid = 4 (val = 9) > 7 -> Discard right half, R = mid - 1 = 3
L = 3, R = 3, mid = 3 (val = 7) == 7 -> FOUND at index 3
```

### 🛠️ Standard Template
```python
def binary_search(nums, target):
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = L + (R - L) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return L  # Insertion index if not found
```

### 📚 Implemented Problems (5)
1. **Count Negative Numbers in a Sorted Matrix (LC 1351)**: [`1351-count-negative-numbers-in-a-sorted-matrix.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/1351-count-negative-numbers-in-a-sorted-matrix.md) | [`1351-count-negative-numbers-in-a-sorted-matrix.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/1351-count-negative-numbers-in-a-sorted-matrix.py)
2. **Search Insert Position (LC 35)**: [`35-search-insert-position.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/35-search-insert-position.md) | [`35-search-insert-position.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/35-search-insert-position.py)
3. **Guess Number Higher or Lower (LC 374)**: [`374-guess-number-higher-or-lower.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/374-guess-number-higher-or-lower.md) | [`374-guess-number-higher-or-lower.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/374-guess-number-higher-or-lower.py)
4. **Sqrt(x) (LC 69)**: [`69-sqrtx.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/69-sqrtx.md) | [`69-sqrtx.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/69-sqrtx.py)
5. **Binary Search (LC 704)**: [`704-binary-search.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/704-binary-search.md) | [`704-binary-search.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-binary-search/problems/704-binary-search.py)

---

## 04. Fast & Slow Pointers

### 💡 Mental Model & Intuition
Floyd's Tortoise & Hare algorithm.
- `slow` takes 1 step at a time; `fast` takes 2 steps at a time.
- If there is a cycle, the distance between them reduces by 1 on every step until they must collide.
- Finding the cycle entry node: After collision, reset `slow` to head; move both 1 step at a time until they meet at the cycle entry.

```text
Head -> [ 1 ] -> [ 2 ] -> [ 3 ] -> [ 4 ]
                           ^         |
                           +-- [ 5 ]-+
```

### 🛠️ Standard Template
```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 📚 Implemented Problems (4)
1. **Linked List Cycle (LC 141)**: [`141-linked-list-cycle.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/141-linked-list-cycle.md) | [`141-linked-list-cycle.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/141-linked-list-cycle.py)
2. **Linked List Cycle II (LC 142)**: [`142-linked-list-cycle-ii.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/142-linked-list-cycle-ii.md) | [`142-linked-list-cycle-ii.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/142-linked-list-cycle-ii.py)
3. **Find the Duplicate Number (LC 287)**: [`287-find-the-duplicate-number.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/287-find-the-duplicate-number.md) | [`287-find-the-duplicate-number.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/287-find-the-duplicate-number.py)
4. **Middle of the Linked List (LC 876)**: [`876-middle-of-the-linked-list.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/876-middle-of-the-linked-list.md) | [`876-middle-of-the-linked-list.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/03-fast-slow-pointers/problems/876-middle-of-the-linked-list.py)

---

## 05. Prefix Sum

### 💡 Mental Model & Intuition
Precomputing cumulative sums or products allows any range query `sum(i..j)` to be answered in $O(1)$ time via `prefix[j] - prefix[i-1]`.
For products without division (LC 238), combine running prefix products from left and suffix products from right.

### 📚 Implemented Problems (1)
1. **Product of Array Except Self (LC 238)**: [`238-product-of-array-except-self.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/04-prefix-sum/problems/238-product-of-array-except-self.md) | [`238-product-of-array-except-self.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/04-prefix-sum/problems/238-product-of-array-except-self.py)

---

## 06. HashMap / Frequency Map

### 💡 Mental Model & Intuition
Trading $O(n)$ space to gain $O(1)$ lookup time:
1. **Complement Matching:** Storing `target - x` to find pairs in one pass.
2. **Frequency Counting & Anagram Signatures:** Character counts as hash keys.
3. **Subarray Sum Equals K:** Storing running prefix sums in a frequency map to count subarrays satisfying `curr_sum - target == prev_sum`.

### 📚 Implemented Problems (8)
1. **Two Sum (LC 1)**: [`1-two-sum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/1-two-sum.md) | [`1-two-sum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/1-two-sum.py)
2. **Longest Consecutive Sequence (LC 128)**: [`128-longest-consecutive-sequence.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/128-longest-consecutive-sequence.md) | [`128-longest-consecutive-sequence.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/128-longest-consecutive-sequence.py)
3. **Single Number (LC 136)**: [`136-single-number.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/136-single-number.md) | [`136-single-number.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/136-single-number.py)
4. **Contains Duplicate (LC 217)**: [`217-contains-duplicate.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/217-contains-duplicate.md) | [`217-contains-duplicate.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/217-contains-duplicate.py)
5. **Valid Anagram (LC 242)**: [`242-valid-anagram.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/242-valid-anagram.md) | [`242-valid-anagram.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/242-valid-anagram.py)
6. **Top K Frequent Elements (LC 347)**: [`347-top-k-frequent-elements.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/347-top-k-frequent-elements.md) | [`347-top-k-frequent-elements.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/347-top-k-frequent-elements.py)
7. **Group Anagrams (LC 49)**: [`49-group-anagrams.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/49-group-anagrams.md) | [`49-group-anagrams.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/49-group-anagrams.py)
8. **Subarray Sum Equals K (LC 560)**: [`560-subarray-sum-equals-k.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/560-subarray-sum-equals-k.md) | [`560-subarray-sum-equals-k.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/05-hashmap-frequency-map/problems/560-subarray-sum-equals-k.py)

---

## 06. Monotonic Stack

### 💡 Mental Model & Intuition
A waiting room of **unresolved elements**. 
- **Monotonic Decreasing Stack:** Finds the **Next Greater Element**. When a larger number arrives, it pops and resolves all smaller elements waiting on the stack.
- **Monotonic Increasing Stack:** Finds the **Next Smaller Element** (used to bound rectangle widths in histograms).

```text
Elements: [ 2, 1, 5, 3, 6 ]
Processing 5:
5 > 1 -> Pop 1 (answer for 1 is 5)
5 > 2 -> Pop 2 (answer for 2 is 5)
Push 5 -> Stack: [5]
```

### 🛠️ Standard Template
```python
def next_greater_elements(nums):
    res = [-1] * len(nums)
    stack = []  # Stores indices
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            prev_idx = stack.pop()
            res[prev_idx] = x
        stack.append(i)
    return res
```

### 📚 Implemented Problems (6)
1. **Sliding Window Maximum (LC 239)**: [`239-sliding-window-maximum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/239-sliding-window-maximum.md) | [`239-sliding-window-maximum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/239-sliding-window-maximum.py)
2. **Next Greater Element I (LC 496)**: [`496-next-greater-element-i.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/496-next-greater-element-i.md) | [`496-next-greater-element-i.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/496-next-greater-element-i.py)
3. **Next Greater Element II (LC 503)**: [`503-next-greater-element-ii.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/503-next-greater-element-ii.md) | [`503-next-greater-element-ii.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/503-next-greater-element-ii.py)
4. **Daily Temperatures (LC 739)**: [`739-daily-temperatures.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/739-daily-temperatures.md) | [`739-daily-temperatures.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/739-daily-temperatures.py)
5. **Largest Rectangle in Histogram (LC 84)**: [`84-largest-rectangle-in-histogram.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/84-largest-rectangle-in-histogram.md) | [`84-largest-rectangle-in-histogram.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/84-largest-rectangle-in-histogram.py)
6. **Online Stock Span (LC 901)**: [`901-online-stock-span.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/901-online-stock-span.md) | [`901-online-stock-span.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/06-monotonic-stack/problems/901-online-stock-span.py)

---

## 07. BFS / Level Order Traversal

### 💡 Mental Model & Intuition
Ripples expanding in a pond. Using a FIFO queue (`collections.deque`), BFS visits all neighbors at distance $d$ before any neighbor at distance $d+1$.
- **Shortest path** in unweighted graphs/grids.
- **Multi-Source BFS:** Push all source nodes into the queue at $t=0$ (e.g., Rotting Oranges, 01-Matrix).

```text
Level 0:        [ 1 ]
               /     \
Level 1:    [ 2 ]   [ 3 ]
            /   \       \
Level 2:  [ 4 ] [ 5 ]   [ 6 ]
```

### 🛠️ Standard Template
```python
from collections import deque

def level_order_bfs(root):
    if not root:
        return []
    q = deque([root])
    levels = []
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(current_level)
    return levels
```

### 📚 Implemented Problems (9)
1. **Binary Tree Level Order Traversal (LC 102)**: [`102-binary-tree-level-order-traversal.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/102-binary-tree-level-order-traversal.md) | [`102-binary-tree-level-order-traversal.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/102-binary-tree-level-order-traversal.py)
2. **Binary Tree Zigzag Level Order Traversal (LC 103)**: [`103-binary-tree-zigzag-level-order-traversal.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/103-binary-tree-zigzag-level-order-traversal.md) | [`103-binary-tree-zigzag-level-order-traversal.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/103-binary-tree-zigzag-level-order-traversal.py)
3. **Word Ladder (LC 127)**: [`127-word-ladder.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/127-word-ladder.md) | [`127-word-ladder.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/127-word-ladder.py)
4. **Map of Highest Peak (LC 1765)**: [`1765-map-of-highest-peak.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/1765-map-of-highest-peak.md) | [`1765-map-of-highest-peak.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/1765-map-of-highest-peak.py)
5. **Binary Tree Right Side View (LC 199)**: [`199-binary-tree-right-side-view.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/199-binary-tree-right-side-view.md) | [`199-binary-tree-right-side-view.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/199-binary-tree-right-side-view.py)
6. **Minimum Genetic Mutation (LC 433)**: [`433-minimum-genetic-mutation.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/433-minimum-genetic-mutation.md) | [`433-minimum-genetic-mutation.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/433-minimum-genetic-mutation.py)
7. **01 Matrix (LC 542)**: [`542-01-matrix.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/542-01-matrix.md) | [`542-01-matrix.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/542-01-matrix.py)
8. **Average of Levels in Binary Tree (LC 637)**: [`637-average-of-levels-in-binary-tree.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/637-average-of-levels-in-binary-tree.md) | [`637-average-of-levels-in-binary-tree.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/637-average-of-levels-in-binary-tree.py)
9. **Rotting Oranges (LC 994)**: [`994-rotting-oranges.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/994-rotting-oranges.md) | [`994-rotting-oranges.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/07-bfs-level-order/problems/994-rotting-oranges.py)

---

## 08. DFS / Backtracking

### 💡 Mental Model & Intuition
Exploring a branch to its deepest leaf before backtracking.
- In **Tree DFS**: Post-order traversal (bottom-up) computes sub-tree heights, balances, or diameters and returns information upward to parent nodes.

### 📚 Implemented Problems (4)
1. **Maximum Depth of Binary Tree (LC 104)**: [`104-maximum-depth-of-binary-tree.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/104-maximum-depth-of-binary-tree.md) | [`104-maximum-depth-of-binary-tree.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/104-maximum-depth-of-binary-tree.py)
2. **Balanced Binary Tree (LC 110)**: [`110-balanced-binary-tree.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/110-balanced-binary-tree.md) | [`110-balanced-binary-tree.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/110-balanced-binary-tree.py)
3. **Path Sum (LC 112)**: [`112-path-sum.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/112-path-sum.md) | [`112-path-sum.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/112-path-sum.py)
4. **Diameter of Binary Tree (LC 543)**: [`543-diameter-of-binary-tree.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/543-diameter-of-binary-tree.md) | [`543-diameter-of-binary-tree.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/08-dfs-backtracking/problems/543-diameter-of-binary-tree.py)

---

## 09. Dynamic Programming

### 💡 Mental Model & Intuition
Breaking problems into overlapping subproblems with optimal substructure.
- **Kadane's Algorithm:** At index $i$, either continue the existing subarray (`curr_sum + x`) or start fresh from $x$ (`max(x, curr_sum + x)`).

### 📚 Implemented Problems (1)
1. **Maximum Subarray (LC 53)**: [`53-maximum-subarray.md`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/09-dynamic-programming/problems/53-maximum-subarray.md) | [`53-maximum-subarray.py`](file:///home/afzal/projects/dsa-patterns/dsa-patterns/09-dynamic-programming/problems/53-maximum-subarray.py)

---

## 🚀 Next Patterns on the Roadmap

Here is the exact progression queue to tackle next:

1. **Pattern #10: Greedy (`10-greedy`)** — Making locally optimal choices without looking back (e.g., Jump Game, Gas Station).
2. **Pattern #11: Intervals (`11-intervals`)** — Sorting by start/end times + sweep line (e.g., Merge Intervals, Non-overlapping Intervals, Meeting Rooms).
3. **Pattern #12: Heap / Priority Queue (`12-heap-priority-queue`)** — Top-K elements, streaming medians, K-way merges.
4. **Pattern #13: Graph Patterns (`13-graph-patterns`)**:
   - 14A. Topological Sort (Kahn's Algorithm & DFS Postorder)
   - 14B. Union-Find / Disjoint Set Union (Rank & Path Compression)
   - 14C. Dijkstra's Algorithm (Shortest path in weighted graphs)
5. **Pattern #14: Trie (`14-trie`)** — Prefix trees, autocomplete, word search dictionary trees.
6. **Pattern #15: Bit Manipulation (`15-bit-manipulation`)** — XOR tricks, bit masking, subset generation.
