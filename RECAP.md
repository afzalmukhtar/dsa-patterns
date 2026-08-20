# 🧠 DSA Master Recap: Intuition, Mental Models, Templates & Code Index

Welcome to your comprehensive master revision guide. This document is crafted to be your **ultimate single-source-of-truth for DSA mastery** — providing vivid mental models, algorithmic invariants, production-grade code templates for every approach, active recall revision strategies, and exact links to all **69 implemented problems** across the **10 active patterns**.

---

## 📊 High-Level Mastery Dashboard

| # | Pattern | Implemented Problems | Primary Mental Model | Core Sub-Patterns Covered | Folder Link |
| :-: | :--- | :---: | :--- | :--- | :-: |
| **01** | [**Two Pointers**](#01-two-pointers) | **16** | Two Pointers core model | Greedy Converging Pointers | [📂 `01-two-pointers`](./01-two-pointers/README.md) |
| **02** | [**Sliding Window**](#02-sliding-window) | **15** | Sliding Window core model | Variable Longest Window | [📂 `02-sliding-window`](./02-sliding-window/README.md) |
| **03** | [**Binary Search**](#03-binary-search) | **5** | Binary Search core model | Staircase / Binary Search | [📂 `03-binary-search`](./03-binary-search/README.md) |
| **04** | [**Fast & Slow Pointers (Hare & Tortoise)**](#04-fast--slow-pointers-hare--tortoise) | **4** | Fast & Slow Pointers (Hare & Tortoise) core model | Cycle Detection (Tortoise & Hare) | [📂 `03-fast-slow-pointers`](./03-fast-slow-pointers/README.md) |
| **05** | [**Prefix Sum**](#05-prefix-sum) | **1** | Prefix Sum core model | Prefix & Suffix Product Accumulation | [📂 `04-prefix-sum`](./04-prefix-sum/README.md) |
| **06** | [**HashMap / Frequency Map**](#06-hashmap--frequency-map) | **8** | HashMap / Frequency Map core model | Complement Hash Lookup | [📂 `05-hashmap-frequency-map`](./05-hashmap-frequency-map/README.md) |
| **07** | [**Monotonic Stack**](#07-monotonic-stack) | **6** | Monotonic Stack core model | Monotonic Decreasing Deque | [📂 `06-monotonic-stack`](./06-monotonic-stack/README.md) |
| **08** | [**BFS / Level Order Traversal**](#08-bfs--level-order-traversal) | **9** | BFS / Level Order Traversal core model | Level Snapshot BFS | [📂 `07-bfs-level-order`](./07-bfs-level-order/README.md) |
| **09** | [**DFS / Backtracking**](#09-dfs--backtracking) | **4** | DFS / Backtracking core model | Bottom-Up Postorder DFS | [📂 `08-dfs-backtracking`](./08-dfs-backtracking/README.md) |
| **10** | [**Dynamic Programming**](#10-dynamic-programming) | **1** | Dynamic Programming core model | Kadane 1D Local/Global DP | [📂 `09-dynamic-programming`](./09-dynamic-programming/README.md) |
| **11-16** | [**Roadmap (Upcoming)**](#-roadmap-patterns-11--16) | *Queued* | Greedy, Intervals, Heaps/PQ, Graph Patterns, Tries, Bit Manipulation | Ready for implementation | [📂 Practice Trackers](./practice/) |

**Total Solutions Implemented:** **69 Problems** (Markdown Explanations + Python Solutions)  
**Curated Roadmaps:** [🎯 Blind 75 Mapping](./practice/blind75.md) | [🎯 NeetCode 150 Mapping](./practice/neetcode150.md)

---

## 🧭 The Intuitive Learning & Active Recall System

### 1. The 3-Second Pattern Recognition Matrix

When you read a coding problem, do not immediately jump to code. Match the **problem signals** against this decision table:

```text
                                      WHAT IS THE PROBLEM ASKING FOR?
                                                    │
        ┌─────────────────────────┬─────────────────┴─────────────────┬─────────────────────────┐
        ▼                         ▼                                   ▼                         ▼
 Contiguous Subarray?      Find Pairs/Triplets?              Next Greater/Smaller?       Shortest Steps / Tree View?
        │                         │                                   │                         │
  Is window size            Is data sorted?                     Unresolved past?           Level-by-level /
  fixed or dynamic?               │                                   │                    unweighted grid?
        │                   ┌─────┴─────┐                             ▼                         │
 ┌──────┴──────┐           YES          NO                     MONOTONIC STACK                  ▼
 ▼             ▼            │            │                                                     BFS
Fixed      Variable         ▼            ▼
SLIDING    SLIDING      TWO POINTERS   HASHMAP
WINDOW     WINDOW       (or Sort 1st)  (Complement)
```

| If the problem mentions... | And the input structure has... | Primary Pattern | Secondary Pattern / Alternative |
| :--- | :--- | :--- | :--- |
| Pair sum, 3Sum, Palindrome, In-place removal | Sorted array, or two-end symmetry | **Two Pointers** | HashMap (if unsorted & extra space allowed) |
| Longest / shortest substring, contiguous subarray | Contiguous items, running constraint ($k$ zeros, unique chars) | **Sliding Window** | Prefix Sum (if negative numbers prevent window monotonicity) |
| Exact value, boundary condition, min speed / max capacity | Monotonic space (`False...False True...True`), sorted input | **Binary Search** | Linear Scan (Brute Force) |
| Cycle in list/array, linked list midpoint, duplicate in $[1..n]$ | Pointer chains, node pointers, value-to-index mapping | **Fast & Slow Pointers** | HashSet (costs $O(n)$ space) |
| Instant range sum query, subarray sum equals $k$ | Static array, cumulative sums, no division allowed | **Prefix Sum** | Sliding Window (only if all elements are positive) |
| "Have I seen this?", exact count, group words, Top-K | Unsorted elements, pair matching, frequency counting | **HashMap / Set** | Bucket Sort / Sorting |
| Next warmer day, largest rectangle, nearest smaller element | Unresolved elements waiting for their right-side answer | **Monotonic Stack** | Monotonic Deque (if sliding window bounded) |
| Shortest transformation, level-order tree traversal, multi-fire | Unweighted graph, grid expansion, layer-by-layer views | **BFS (Queue)** | Multi-Source BFS (seed all $t=0$ sources) |
| All combinations, all permutations, tree height/diameter | Exhaustive search, tree recursion, path checking | **DFS / Backtracking** | Bottom-up postorder / Top-down pre-order |
| Count ways, min cost, max profit, overlapping subproblems | Subproblems build upon earlier states, optimal choices | **Dynamic Programming** | Top-Down Memoization or Bottom-Up Tabulation |

---

### 2. The Universal 5-Step Interview Solving Protocol

1. **Clarify Constraints & Edge Cases (1-2 mins)**:
   - Array size $n$ ($n \le 10^5 \implies O(n)$ or $O(n \log n)$; $n \le 10^3 \implies O(n^2)$; $n \le 20 \implies O(2^n)$ backtracking).
   - Can elements be negative? Are there duplicate values? Can the input be empty or have 1 element?

2. **State the Brute Force & Isolate the Bottleneck (1 min)**:
   - *"Brute force is checking every pair/window in $O(n^2)$. The bottleneck is re-scanning already visited elements."*

3. **Select Pattern & State the Core Invariant (1 min)**:
   - State the **invariant**: *"By keeping $L$ and $R$, we eliminate half the search space because sorting guarantees moving $R$ left strictly decreases the sum."*

4. **Implement Cleanly with Standard Templates (5-10 mins)**:
   - Use standardized pointer names (`L`, `R`, `slow`, `fast`), loop bounds, and guard clauses.

5. **Trace Edge Cases & Verify Big-O ($T$ and $S$) (2 mins)**:
   - Walk through a small test case (e.g., `[1, 2]`, single element, all duplicates).


---

### 3. Spaced Revision & Active Recall Rules

> [!TIP]
> **The 1-Sentence "Feynman" Rule:** For every problem you solve, you should be able to explain the core insight to a 10-year-old in one sentence without touching code.

- **Day 1:** Implement and understand the core template.
- **Day 3:** Revisit the problem title and write down *only* the **Invariant** and **Sub-pattern** on paper.
- **Day 7:** Re-implement the solution from scratch in under 7 minutes without looking at references.
- **Day 30:** Practice random selection from Blind 75 / NeetCode 150.


---

## 01. Two Pointers

> **Pattern Folder:** [📂 `01-two-pointers`](./01-two-pointers/README.md) | **Implemented Solutions:** 16 Problems

### 💡 Mental Model & Intuition
Imagine two runners on a track.
1. **Opposite-End Convergence (`L = 0`, `R = n - 1`)**: Like squeezing an accordion. Because the data is sorted, `nums[L] + nums[R]` gives you a **compass**: if the sum is too large, decrement `R`; if too small, increment `L`. Every step eliminates an entire row/column of redundant pairs without checking them.
2. **Same-Direction / Fast-Slow Read-Write (`slow = 0`, `fast = 0`)**: `fast` acts as a scout scanning the array, while `slow` acts as a builder writing only valid/filtered elements in-place.
3. **Dutch National Flag 3-Way Partition (`low`, `mid`, `high`)**: `mid` scans the array. 0s are thrown left (`low`), 2s are thrown right (`high`), and 1s remain in the middle.

```text
Opposite-Ends (Sorted 2Sum):
[ 1,   3,   5,   7,   9,   11 ]   Target = 10
  L                         R     -> 1 + 11 = 12 (> 10, decrement R)
  L                    R          -> 1 + 9  = 10 (MATCH! Return [L, R])

Same-Direction (Remove Duplicates):
[ 1,   1,   2,   2,   3 ]
  S,F                         nums[F] == nums[S] -> F advances
  S    F                      nums[F] != nums[S] -> S advances, copy nums[F] to nums[S]
       S    F
```

### 🚨 When to Use
- Sorted array pair sums, 3Sum, 4Sum.
- Palindrome validation (reading forward and backward simultaneously).
- In-place array modification ($O(1)$ space requirement).
- Trapping rain water / container boundaries.

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Opposite-Ends Convergence
```python
def two_pointers_opposite(nums: list[int], target: int) -> list[int]:
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

#### Template 2: Same-Direction In-Place Read-Write
```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

#### Template 3: 3Sum (Fixed Element + Converging Pointers + Deduplication)
```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate fixed elements
        L, R = i + 1, len(nums) - 1
        while L < R:
            total = nums[i] + nums[L] + nums[R]
            if total == 0:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]: L += 1  # Skip duplicate L
                while L < R and nums[R] == nums[R - 1]: R -= 1  # Skip duplicate R
                L += 1
                R -= 1
            elif total < 0:
                L += 1
            else:
                R -= 1
    return res
```

#### Template 4: Dutch National Flag (3-Way Partitioning)
```python
def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1  # Do NOT advance mid; newly swapped element must be inspected!
```

### ⚠️ Edge Cases & Invariants
- **Duplicate Skipping in 3Sum/4Sum**: Always skip duplicates *after* recording a match for `L` and `R`, and skip at the top of the outer loop (`i > 0 and nums[i] == nums[i-1]`).
- **Mid Pointer in Dutch Flag**: When swapping `nums[mid]` with `nums[high]`, do **not** increment `mid` because the swapped element from `high` has not been evaluated yet!
- **Container Water Invariant**: Always move the pointer pointing to the **shorter line**. Moving the taller line cannot increase the area because width decreases and height is bounded by the shorter line.

---

### 📚 Problem Catalog & Code Links (16 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 11 | [`📄 LC 11: Container With Most Water`](./01-two-pointers/problems/11-container-with-most-water.md) | [`💻 11-container-with-most-water.py`](./01-two-pointers/problems/11-container-with-most-water.py) | Greedy Converging Pointers | Move the shorter wall inward; moving taller wall only shrinks width without height gain | $O(n)$ | $O(1)$ |
| 125 | [`📄 LC 125: Valid Palindrome`](./01-two-pointers/problems/125-valid-palindrome.md) | [`💻 125-valid-palindrome.py`](./01-two-pointers/problems/125-valid-palindrome.py) | Opposite-Ends Convergence | Skip non-alphanumeric chars; check s[L].lower() == s[R].lower() | $O(n)$ | $O(1)$ |
| 15 | [`📄 LC 15: 3Sum`](./01-two-pointers/problems/15-3sum.md) | [`💻 15-3sum.py`](./01-two-pointers/problems/15-3sum.py) | Fixed Element + 2P | Sort array first; fix index i, run 2-pointer on remainder; skip duplicate elements at all levels | $O(n^2)$ | $O(1)$ |
| 16 | [`📄 LC 16: 3Sum Closest`](./01-two-pointers/problems/16-3sum-closest.md) | [`💻 16-3sum-closest.py`](./01-two-pointers/problems/16-3sum-closest.py) | Fixed Element + 2P | Track minimum abs(total - target) while moving converging pointers toward target | $O(n^2)$ | $O(1)$ |
| 167 | [`📄 LC 167: Two Sum II - Input Array Is Sorted`](./01-two-pointers/problems/167-two-sum-ii-input-array-is-sorted.md) | [`💻 167-two-sum-ii-input-array-is-sorted.py`](./01-two-pointers/problems/167-two-sum-ii-input-array-is-sorted.py) | Opposite-Ends Convergence | Sum too big -> R--; sum too small -> L++ | $O(n)$ | $O(1)$ |
| 18 | [`📄 LC 18: 4Sum`](./01-two-pointers/problems/18-4sum.md) | [`💻 18-4sum.py`](./01-two-pointers/problems/18-4sum.py) | 2 Fixed Elements + 2P | Two nested loops + 2-pointer scan; deduplicate at all four pointer levels | $O(n^3)$ | $O(1)$ |
| 19 | [`📄 LC 19: Remove Nth Node From End of List`](./01-two-pointers/problems/19-remove-nth-node-from-end-of-list.md) | [`💻 19-remove-nth-node-from-end-of-list.py`](./01-two-pointers/problems/19-remove-nth-node-from-end-of-list.py) | Fixed-Gap Pointers | Advance fast N+1 steps ahead with dummy head, then advance both until fast is None | $O(n)$ | $O(1)$ |
| 26 | [`📄 LC 26: Remove Duplicates from Sorted Array`](./01-two-pointers/problems/26-remove-duplicates-from-sorted-array.md) | [`💻 26-remove-duplicates-from-sorted-array.py`](./01-two-pointers/problems/26-remove-duplicates-from-sorted-array.py) | Same-Direction Read/Write | Write to slow only when nums[fast] != nums[slow] | $O(n)$ | $O(1)$ |
| 27 | [`📄 LC 27: Remove Element`](./01-two-pointers/problems/27-remove-element.md) | [`💻 27-remove-element.py`](./01-two-pointers/problems/27-remove-element.py) | Same-Direction Read/Write | If nums[fast] != val, write to nums[slow] and increment slow | $O(n)$ | $O(1)$ |
| 283 | [`📄 LC 283: Move Zeroes`](./01-two-pointers/problems/283-move-zeroes.md) | [`💻 283-move-zeroes.py`](./01-two-pointers/problems/283-move-zeroes.py) | Same-Direction Swap | Swap non-zero at fast with slow, increment slow | $O(n)$ | $O(1)$ |
| 344 | [`📄 LC 344: Reverse String`](./01-two-pointers/problems/344-reverse-string.md) | [`💻 344-reverse-string.py`](./01-two-pointers/problems/344-reverse-string.py) | Opposite-Ends Swap | Swap s[L] and s[R], move inward until L >= R | $O(n)$ | $O(1)$ |
| 345 | [`📄 LC 345: Reverse Vowels of a String`](./01-two-pointers/problems/345-reverse-vowels-of-a-string.md) | [`💻 345-reverse-vowels-of-a-string.py`](./01-two-pointers/problems/345-reverse-vowels-of-a-string.py) | Opposite-Ends Vowel Search | Advance L and R until both hit vowels, then swap | $O(n)$ | $O(n)$ |
| 42 | [`📄 LC 42: Trapping Rain Water`](./01-two-pointers/problems/42-trapping-rain-water.md) | [`💻 42-trapping-rain-water.py`](./01-two-pointers/problems/42-trapping-rain-water.py) | Converging Max-Track | Water trapped is bounded by min(max_L, max_R) - height[i]; process smaller side | $O(n)$ | $O(1)$ |
| 680 | [`📄 LC 680: Valid Palindrome II`](./01-two-pointers/problems/680-valid-palindrome-ii.md) | [`💻 680-valid-palindrome-ii.py`](./01-two-pointers/problems/680-valid-palindrome-ii.py) | Branching Palindrome | On first mismatch s[L] != s[R], check if either s[L+1..R] or s[L..R-1] is palindrome | $O(n)$ | $O(1)$ |
| 75 | [`📄 LC 75: Sort Colors`](./01-two-pointers/problems/75-sort-colors.md) | [`💻 75-sort-colors.py`](./01-two-pointers/problems/75-sort-colors.py) | Dutch National Flag 3-Way | Maintain [0..low-1] as 0s, [high+1..n-1] as 2s, scan with mid | $O(n)$ | $O(1)$ |
| 80 | [`📄 LC 80: Remove Duplicates from Sorted Array II`](./01-two-pointers/problems/80-remove-duplicates-from-sorted-array-ii.md) | [`💻 80-remove-duplicates-from-sorted-array-ii.py`](./01-two-pointers/problems/80-remove-duplicates-from-sorted-array-ii.py) | Same-Direction K-Lookback | Allow up to 2 duplicates by checking nums[fast] != nums[slow - 2] | $O(n)$ | $O(1)$ |

---

## 02. Sliding Window

> **Pattern Folder:** [📂 `02-sliding-window`](./02-sliding-window/README.md) | **Implemented Solutions:** 15 Problems

### 💡 Mental Model & Intuition
Think of looking at scenery through a camera viewfinder sliding over a panorama.
- **Fixed Window ($k$)**: The window frame is locked to width $k$. As it moves 1 unit right, exactly **one element leaves on the left (`nums[i-k]`)** and **one element enters on the right (`nums[i]`)**. Running stats update in $O(1)$ rather than recalculating all $k$ elements ($O(k)$).
- **Dynamic Variable Window**:
  - *Expanding (`R` moves right)*: Greedily add elements to satisfy the condition or explore bigger windows.
  - *Shrinking (`L` moves right)*: When a constraint is broken (e.g., > $k$ zeros, duplicate char, sum $\\ge$ target), shrink the left side until the window is valid again.

```text
Fixed Window (k = 3):
[ 2,  1,  5,  1,  3,  2 ]
 [2,  1,  5]              -> sum = 8
     [1,  5,  1]          -> sum = 8 - 2 + 1 = 7 (O(1) update!)

Variable Window (Longest Substring Without Repeating Characters):
\" a   b   c   a   b   c   b   b \"
 [a   b   c]                         len = 3, state = {a, b, c}
 [a   b   c   a]                     'a' duplicated! Shrink L past first 'a'
     [b   c   a]                     len = 3, valid again
```

### 🚨 When to Use
- Contiguous subarray or substring problems.
- Finding longest/shortest window satisfying a constraint (sum, character counts, distinct elements).
- Substring pattern matching (Anagrams, Permutations, Minimum Window).

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Fixed Window of Size k
```python
def fixed_sliding_window(nums: list[int], k: int) -> int:
    curr_sum = sum(nums[:k])
    best = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]  # Add incoming, subtract outgoing
        best = max(best, curr_sum)
    return best
```

#### Template 2: Variable Window — Longest Subarray / Substring
```python
def variable_window_longest(s: str) -> int:
    L = 0
    state = {}
    max_len = 0
    for R in range(len(s)):
        # 1. Expand: include s[R]
        state[s[R]] = state.get(s[R], 0) + 1
        
        # 2. Shrink: while window is INVALID, evict from left
        while is_invalid(state):
            state[s[L]] -= 1
            if state[s[L]] == 0:
                del state[s[L]]
            L += 1
            
        # 3. Update answer: window is guaranteed VALID here
        max_len = max(max_len, R - L + 1)
    return max_len
```

#### Template 3: Variable Window — Shortest Subarray
```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    L = 0
    curr_sum = 0
    min_len = float('inf')
    for R in range(len(nums)):
        curr_sum += nums[R]
        # Shrink as long as condition IS MET to find minimum length
        while curr_sum >= target:
            min_len = min(min_len, R - L + 1)
            curr_sum -= nums[L]
            L += 1
    return min_len if min_len != float('inf') else 0
```

#### Template 4: Exact Frequency / Matching Window (Minimum Window Substring)
```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s: return ''
    target_counts = Counter(t)
    window_counts = {}
    have, need = 0, len(target_counts)
    res, res_len = [-1, -1], float('inf')
    L = 0
    
    for R in range(len(s)):
        char = s[R]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            have += 1
            
        while have == need:
            if (R - L + 1) < res_len:
                res = [L, R]
                res_len = R - L + 1
            # Evict from left
            left_char = s[L]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                have -= 1
            L += 1
            
    L, R = res
    return s[L:R+1] if res_len != float('inf') else ''
```

### ⚠️ Edge Cases & Invariants
- **Longest vs. Shortest Answer Recording**: For *Longest Subarray*, record answer **after** the `while` shrink loop. For *Shortest Subarray*, record answer **inside** the `while` shrink loop.
- **Subarrays Count Formula**: The number of new valid subarrays ending at index $R$ is exactly `R - L + 1`.
- **Negative Numbers**: If an array has negative values, sliding window monotonicity breaks — use Prefix Sum + HashMap instead.

---

### 📚 Problem Catalog & Code Links (15 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 1004 | [`📄 LC 1004: Max Consecutive Ones III`](./02-sliding-window/problems/1004-max-consecutive-ones-iii.md) | [`💻 1004-max-consecutive-ones-iii.py`](./02-sliding-window/problems/1004-max-consecutive-ones-iii.py) | Variable Longest Window | Allow at most k zeros in window; shrink L when zeros count > k | $O(n)$ | $O(1)$ |
| 121 | [`📄 LC 121: Best Time to Buy and Sell Stock`](./02-sliding-window/problems/121-best-time-to-buy-and-sell-stock.md) | [`💻 121-best-time-to-buy-and-sell-stock.py`](./02-sliding-window/problems/121-best-time-to-buy-and-sell-stock.py) | Dynamic Low Tracker | If price[R] < price[L], reset buy day L = R; else calculate profit | $O(n)$ | $O(1)$ |
| 1343 | [`📄 LC 1343: Number of Sub-arrays of Size K and Avg >= Threshold`](./02-sliding-window/problems/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.md) | [`💻 1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py`](./02-sliding-window/problems/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py) | Fixed Window (k) | Maintain sum over size k; check win_sum >= k * threshold | $O(n)$ | $O(1)$ |
| 1456 | [`📄 LC 1456: Maximum Number of Vowels in Substring of Length K`](./02-sliding-window/problems/1456-maximum-number-of-vowels-in-a-substring-of-given-length.md) | [`💻 1456-maximum-number-of-vowels-in-a-substring-of-given-length.py`](./02-sliding-window/problems/1456-maximum-number-of-vowels-in-a-substring-of-given-length.py) | Fixed Window (k) | Add 1 if incoming char is vowel; subtract 1 if outgoing char is vowel | $O(n)$ | $O(1)$ |
| 1493 | [`📄 LC 1493: Longest Subarray of 1s After Deleting One Element`](./02-sliding-window/problems/1493-longest-subarray-of-1s-after-deleting-one-element.md) | [`💻 1493-longest-subarray-of-1s-after-deleting-one-element.py`](./02-sliding-window/problems/1493-longest-subarray-of-1s-after-deleting-one-element.py) | Variable Longest Window | Window can contain at most 1 zero; answer is max(R - L) (implicitly deleted) | $O(n)$ | $O(1)$ |
| 1876 | [`📄 LC 1876: Substrings of Size Three with Distinct Characters`](./02-sliding-window/problems/1876-substrings-of-size-three-with-distinct-characters.md) | [`💻 1876-substrings-of-size-three-with-distinct-characters.py`](./02-sliding-window/problems/1876-substrings-of-size-three-with-distinct-characters.py) | Fixed Window (k=3) | Check if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2] | $O(n)$ | $O(1)$ |
| 209 | [`📄 LC 209: Minimum Size Subarray Sum`](./02-sliding-window/problems/209-minimum-size-subarray-sum.md) | [`💻 209-minimum-size-subarray-sum.py`](./02-sliding-window/problems/209-minimum-size-subarray-sum.py) | Variable Shortest Window | Expand R until sum >= target; shrink L while recording minimum length | $O(n)$ | $O(1)$ |
| 2461 | [`📄 LC 2461: Maximum Sum of Distinct Subarrays With Length K`](./02-sliding-window/problems/2461-maximum-sum-of-distinct-subarrays-with-length-k.md) | [`💻 2461-maximum-sum-of-distinct-subarrays-with-length-k.py`](./02-sliding-window/problems/2461-maximum-sum-of-distinct-subarrays-with-length-k.py) | Fixed Window + Set/Map | Fixed size k window; valid only when len(freq_map) == k | $O(n)$ | $O(k)$ |
| 3 | [`📄 LC 3: Longest Substring Without Repeating Characters`](./02-sliding-window/problems/3-longest-substring-without-repeating-characters.md) | [`💻 3-longest-substring-without-repeating-characters.py`](./02-sliding-window/problems/3-longest-substring-without-repeating-characters.py) | Variable Longest Window | Map stores last seen index; jump L = max(L, last[c] + 1) | $O(n)$ | $O(min(n, m))$ |
| 438 | [`📄 LC 438: Find All Anagrams in a String`](./02-sliding-window/problems/438-find-all-anagrams-in-a-string.md) | [`💻 438-find-all-anagrams-in-a-string.py`](./02-sliding-window/problems/438-find-all-anagrams-in-a-string.py) | Fixed Frequency Match | Match array of size 26; compare window freq with pattern freq | $O(n)$ | $O(1)$ |
| 567 | [`📄 LC 567: Permutation in String`](./02-sliding-window/problems/567-permutation-in-string.md) | [`💻 567-permutation-in-string.py`](./02-sliding-window/problems/567-permutation-in-string.py) | Fixed Frequency Match | Maintain count of 26-char matches; return True if matches == 26 | $O(n)$ | $O(1)$ |
| 643 | [`📄 LC 643: Maximum Average Subarray I`](./02-sliding-window/problems/643-maximum-average-subarray-i.md) | [`💻 643-maximum-average-subarray-i.py`](./02-sliding-window/problems/643-maximum-average-subarray-i.py) | Fixed Window (k) | Keep running sum for k elements; return max_sum / k | $O(n)$ | $O(1)$ |
| 713 | [`📄 LC 713: Subarray Product Less Than K`](./02-sliding-window/problems/713-subarray-product-less-than-k.md) | [`💻 713-subarray-product-less-than-k.py`](./02-sliding-window/problems/713-subarray-product-less-than-k.py) | Variable Subarray Count | For each R, divide by nums[L] while product >= k; add R - L + 1 | $O(n)$ | $O(1)$ |
| 76 | [`📄 LC 76: Minimum Window Substring`](./02-sliding-window/problems/76-minimum-window-substring.md) | [`💻 76-minimum-window-substring.py`](./02-sliding-window/problems/76-minimum-window-substring.py) | Variable Shortest Match | Track have == need distinct char counts; contract L while window satisfies | $O(n)$ | $O(m)$ |
| 904 | [`📄 LC 904: Fruit Into Baskets`](./02-sliding-window/problems/904-fruit-into-baskets.md) | [`💻 904-fruit-into-baskets.py`](./02-sliding-window/problems/904-fruit-into-baskets.py) | Variable (Max 2 Types) | Longest subarray with at most 2 distinct keys in frequency map | $O(n)$ | $O(1)$ |

---

## 03. Binary Search

> **Pattern Folder:** [📂 `03-binary-search`](./03-binary-search/README.md) | **Implemented Solutions:** 5 Problems

### 💡 Mental Model & Intuition
Imagine guessing a number between 1 and 100 with 'Higher' or 'Lower' clues. Guessing 50 eliminates half the universe instantly.
Binary Search is **not just for sorted arrays**; it applies to **any search space that exhibits a monotonic Boolean property $P(x)$**:
$$\\underbrace{[\\text{False, False, False}, \\dots, \\text{False}}_{\\text{Invalid Space}}, \\underbrace{\\text{True, True, True}, \\dots, \\text{True}]}_{\\text{Valid Space}}$$
Binary search finds the exact **boundary / transition point** in $O(\\log n)$ comparisons.

```text
Monotonic Boolean Predicate:
Index:   0      1      2      3      4      5
Value: [ 2,     4,     6,     8,    10,    12 ]
>= 7:  [ False, False, False, True,  True,  True ]
                               ^
                       First True (Index 3)
```

### 🚨 When to Use
- Array is sorted or rotated sorted.
- Problem asks for minimum/maximum speed, capacity, days ('Search on Answer Space').
- Expected complexity is $O(\\log n)$.

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Exact Match (while L <= R)
```python
def binary_search_exact(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = L + (R - L) // 2  # Prevents integer overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1
```

#### Template 2: Find Leftmost Boundary / Insertion Position (First True)
```python
def find_first_true(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    res = len(nums)  # Default if no element satisfies
    while L <= R:
        mid = L + (R - L) // 2
        if nums[mid] >= target:  # Condition met: record and try finding earlier on LEFT
            res = mid
            R = mid - 1
        else:
            L = mid + 1
    return res
```

#### Template 3: Binary Search on Answer Space
```python
def search_answer_space(low: int, high: int) -> int:
    res = low
    while low <= high:
        mid = low + (high - low) // 2
        if is_feasible(mid):  # If mid is valid, try optimizing further
            res = mid
            high = mid - 1   # or low = mid + 1 depending on min vs max
        else:
            low = mid + 1
    return res
```

### ⚠️ Edge Cases & Invariants
- **Mid Calculation**: Always use `mid = L + (R - L) // 2` to prevent overflow.
- **Search Insert Rule**: When `while L <= R` terminates without finding `target`, `L` is guaranteed to be the exact **insertion index**.

---

### 📚 Problem Catalog & Code Links (5 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 1351 | [`📄 LC 1351: Count Negative Numbers in a Sorted Matrix`](./03-binary-search/problems/1351-count-negative-numbers-in-a-sorted-matrix.md) | [`💻 1351-count-negative-numbers-in-a-sorted-matrix.py`](./03-binary-search/problems/1351-count-negative-numbers-in-a-sorted-matrix.py) | Staircase / Binary Search | Start from bottom-left or top-right; if negative, all elements below/right are negative | $O(m + n)$ | $O(1)$ |
| 35 | [`📄 LC 35: Search Insert Position`](./03-binary-search/problems/35-search-insert-position.md) | [`💻 35-search-insert-position.py`](./03-binary-search/problems/35-search-insert-position.py) | Boundary Search | Standard binary search; on loop exit (L > R), L is the exact insertion point | $O(log n)$ | $O(1)$ |
| 374 | [`📄 LC 374: Guess Number Higher or Lower`](./03-binary-search/problems/374-guess-number-higher-or-lower.md) | [`💻 374-guess-number-higher-or-lower.py`](./03-binary-search/problems/374-guess-number-higher-or-lower.py) | Interactive Binary Search | Use API response to eliminate half: 0 -> found, -1 -> R = mid - 1, 1 -> L = mid + 1 | $O(log n)$ | $O(1)$ |
| 69 | [`📄 LC 69: Sqrt(x)`](./03-binary-search/problems/69-sqrtx.md) | [`💻 69-sqrtx.py`](./03-binary-search/problems/69-sqrtx.py) | Answer Space Search | Search range [0, x]; if mid^2 <= x, record res = mid and search higher | $O(log x)$ | $O(1)$ |
| 704 | [`📄 LC 704: Binary Search`](./03-binary-search/problems/704-binary-search.md) | [`💻 704-binary-search.py`](./03-binary-search/problems/704-binary-search.py) | Exact Match BS | Textbook classic halving algorithm on sorted array with while L <= R | $O(log n)$ | $O(1)$ |

---

## 04. Fast & Slow Pointers (Hare & Tortoise)

> **Pattern Folder:** [📂 `03-fast-slow-pointers`](./03-fast-slow-pointers/README.md) | **Implemented Solutions:** 4 Problems

### 💡 Mental Model & Intuition
Imagine two runners on a circular track. Runner $F$ runs at speed 2, Runner $S$ runs at speed 1.
1. **Cycle Detection**: On a straight line, $F$ reaches the end. On a loop, the relative distance between $F$ and $S$ increases by 1 on every tick. Thus, $F$ is guaranteed to lap and collide with $S$ without infinite loops.
2. **Cycle Entrance Proof**:
   - Let distance to cycle start $= L$, distance from start to meeting point $= x$, cycle circumference $= C$.
   - Slow ran $L + x$; Fast ran $L + x + kC$.
   - Since $2 \\cdot \\text{dist}(S) = \\text{dist}(F) \\implies 2(L + x) = L + x + kC \\implies L = kC - x$.
   - **Action**: Reset $S$ to head, keep $F$ at meeting point. Move both at speed 1. They meet exactly at the cycle entrance!

```text
Head ──(L steps)──> Entrance ──(x steps)──> Meeting Point
                        ^                         │
                        └───────(C - x steps)─────┘
```

### 🚨 When to Use
- Linked list cycle detection or cycle start node.
- Finding the middle node of a linked list in a single pass.
- Finding duplicate numbers in arrays where values map to indices ($1 \\le \\text{nums}[i] \\le n$).

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Detect Cycle & Find Entry Node
```python
def detect_cycle_entry(head):
    slow = fast = head
    # Phase 1: Detect collision
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
        
    # Phase 2: Find cycle entrance
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

#### Template 2: Find Middle of Linked List
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # For even length, returns the second middle node
```

### ⚠️ Edge Cases & Invariants
- **Collision Guarantee**: If a cycle exists, the gap between fast and slow decreases by 1 modulo cycle length on each step.
- **Midpoint Parity**: `fast and fast.next` ensures slow lands on the second middle node for even lengths.

---

### 📚 Problem Catalog & Code Links (4 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 141 | [`📄 LC 141: Linked List Cycle`](./03-fast-slow-pointers/problems/141-linked-list-cycle.md) | [`💻 141-linked-list-cycle.py`](./03-fast-slow-pointers/problems/141-linked-list-cycle.py) | Cycle Detection (Tortoise & Hare) | If fast == slow, a cycle exists. If fast or fast.next is None, no cycle | $O(n)$ | $O(1)$ |
| 142 | [`📄 LC 142: Linked List Cycle II`](./03-fast-slow-pointers/problems/142-linked-list-cycle-ii.md) | [`💻 142-linked-list-cycle-ii.py`](./03-fast-slow-pointers/problems/142-linked-list-cycle-ii.py) | Cycle Entrance Math | Reset slow to head after collision; move both at speed 1 to intersect at entry | $O(n)$ | $O(1)$ |
| 287 | [`📄 LC 287: Find the Duplicate Number`](./03-fast-slow-pointers/problems/287-find-the-duplicate-number.md) | [`💻 287-find-the-duplicate-number.py`](./03-fast-slow-pointers/problems/287-find-the-duplicate-number.py) | Implicit Array Cycle | Treat nums[i] as pointer next = nums[i]; duplicate value has multiple incoming edges | $O(n)$ | $O(1)$ |
| 876 | [`📄 LC 876: Middle of the Linked List`](./03-fast-slow-pointers/problems/876-middle-of-the-linked-list.md) | [`💻 876-middle-of-the-linked-list.py`](./03-fast-slow-pointers/problems/876-middle-of-the-linked-list.py) | Midpoint Detection | When fast reaches tail, slow has traversed exactly half the distance | $O(n)$ | $O(1)$ |

---

## 05. Prefix Sum

> **Pattern Folder:** [📂 `04-prefix-sum`](./04-prefix-sum/README.md) | **Implemented Solutions:** 1 Problems

### 💡 Mental Model & Intuition
Think of an automobile odometer. To calculate distance between Mile Marker 30 and Mile Marker 80, you don't re-measure the road; you compute $\\text{Odometer}(80) - \\text{Odometer}(29)$.
$$\\text{Sum}(L \\dots R) = \\text{Prefix}[R] - \\text{Prefix}[L-1]$$
For multiplication without division (LC 238), precompute running products from left, then sweep from right accumulating suffix products.

```text
Array:       [  3,   1,   4,   2  ]
Prefix Sum:  [  3,   4,   8,  10  ]
Sum(1..3) = Prefix[3] - Prefix[0] = 10 - 3 = 7 (1 + 4 + 2)
```

### 🚨 When to Use
- Frequent static range sum queries ($O(1)$ query time).
- Subarrays with exact target sums (paired with HashMap: $\\text{curr_sum} - \\text{target} = \\text{earlier_prefix}$).
- Product calculations where division is disallowed.

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Product of Array Except Self (O(1) Extra Space)
```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    # Pass 1: Prefix products into res
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    # Pass 2: Suffix products multiplied on the fly
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res
```

### ⚠️ Edge Cases & Invariants
- **No Division Trick**: Break `res[i]` into `(elements to left) * (elements to right)`.
- **0-Index Offsets**: Prepend a 0 to prefix sums (`len = n + 1`) to eliminate boundary checking for `L = 0`.

---

### 📚 Problem Catalog & Code Links (1 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 238 | [`📄 LC 238: Product of Array Except Self`](./04-prefix-sum/problems/238-product-of-array-except-self.md) | [`💻 238-product-of-array-except-self.py`](./04-prefix-sum/problems/238-product-of-array-except-self.py) | Prefix & Suffix Product Accumulation | res[i] = prefix_product[i-1] * suffix_product[i+1]; compute in two sweeps without division | $O(n)$ | $O(1)$ |

---

## 06. HashMap / Frequency Map

> **Pattern Folder:** [📂 `05-hashmap-frequency-map`](./05-hashmap-frequency-map/README.md) | **Implemented Solutions:** 8 Problems

### 💡 Mental Model & Intuition
Trading $O(n)$ memory to collapse an inner $O(n)$ lookup loop into $O(1)$.
- **Complement Lookup**: *\"I am at $x$. I need $y = \\text{target} - x$. Have I seen $y$ earlier in my memory?\"*
- **Frequency Map & Bucket Sort**: Counting items with a hash map, then grouping elements into buckets by frequency (`bucket[count] = [elements]`) allows finding Top-K elements in $O(n)$ time without a heap.
- **Canonical Key Hashing**: All anagrams have the exact same sorted tuple or 26-element character count tuple.

```text
Two Sum:
target = 9, current num = 7
complement = 9 - 7 = 2
seen = {2: index 0} -> Found instant match! Return [0, current_index]
```

### 🚨 When to Use
- Pair/sum problems on unsorted arrays.
- Anagram detection and grouping.
- Subarray sums equals $k$ with negative numbers present.
- Finding unique elements, duplicates, or longest consecutive runs.

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Instant Complement Matching (Two Sum)
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
```

#### Template 2: Prefix Sum + HashMap (Subarray Sum Equals K)
```python
def subarray_sum_k(nums: list[int], k: int) -> int:
    count = 0
    curr_sum = 0
    seen = {0: 1}  # Seed with base case: prefix sum 0 occurs once
    for x in nums:
        curr_sum += x
        count += seen.get(curr_sum - k, 0)
        seen[curr_sum] = seen.get(curr_sum, 0) + 1
    return count
```

#### Template 3: Top-K Frequent Elements (Bucket Sort O(n))
```python
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for val, freq in count.items():
        buckets[freq].append(val)
    res = []
    for freq in range(len(buckets) - 1, 0, -1):
        for val in buckets[freq]:
            res.append(val)
            if len(res) == k:
                return res
    return res
```

#### Template 4: Longest Consecutive Sequence (O(n) via HashSet)
```python
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0
    for x in num_set:
        # Check if x is the START of a streak (x - 1 not in set)
        if x - 1 not in num_set:
            curr = x
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
    return longest
```

### ⚠️ Edge Cases & Invariants
- **Prefix Sum Hash Seed**: Always initialize `seen = {0: 1}` for prefix sum hashing to account for subarrays starting at index 0.
- **Streak Start Invariant**: Checking `if x - 1 not in num_set` ensures each number is visited at most twice, guaranteeing $O(n)$ overall.

---

### 📚 Problem Catalog & Code Links (8 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 1 | [`📄 LC 1: Two Sum`](./05-hashmap-frequency-map/problems/1-two-sum.md) | [`💻 1-two-sum.py`](./05-hashmap-frequency-map/problems/1-two-sum.py) | Complement Hash Lookup | Store value -> index; check if target - num already in map | $O(n)$ | $O(n)$ |
| 128 | [`📄 LC 128: Longest Consecutive Sequence`](./05-hashmap-frequency-map/problems/128-longest-consecutive-sequence.md) | [`💻 128-longest-consecutive-sequence.py`](./05-hashmap-frequency-map/problems/128-longest-consecutive-sequence.py) | HashSet Streak Start | Only explore streaks starting from numbers where x - 1 is absent | $O(n)$ | $O(n)$ |
| 136 | [`📄 LC 136: Single Number`](./05-hashmap-frequency-map/problems/136-single-number.md) | [`💻 136-single-number.py`](./05-hashmap-frequency-map/problems/136-single-number.py) | Bitwise XOR / Hash | x ^ x = 0 and x ^ 0 = x; XOR-ing all elements leaves single unique | $O(n)$ | $O(1)$ |
| 217 | [`📄 LC 217: Contains Duplicate`](./05-hashmap-frequency-map/problems/217-contains-duplicate.md) | [`💻 217-contains-duplicate.py`](./05-hashmap-frequency-map/problems/217-contains-duplicate.py) | HashSet Existence Check | Insert into set; return True immediately on duplicate hit | $O(n)$ | $O(n)$ |
| 242 | [`📄 LC 242: Valid Anagram`](./05-hashmap-frequency-map/problems/242-valid-anagram.md) | [`💻 242-valid-anagram.py`](./05-hashmap-frequency-map/problems/242-valid-anagram.py) | Frequency Map / Array | Counter(s) == Counter(t) or 26-element array match | $O(n)$ | $O(1)$ |
| 347 | [`📄 LC 347: Top K Frequent Elements`](./05-hashmap-frequency-map/problems/347-top-k-frequent-elements.md) | [`💻 347-top-k-frequent-elements.py`](./05-hashmap-frequency-map/problems/347-top-k-frequent-elements.py) | Bucket Sort / Frequency Map | Frequency map -> index buckets by frequency -> collect Top-K in O(n) | $O(n)$ | $O(n)$ |
| 49 | [`📄 LC 49: Group Anagrams`](./05-hashmap-frequency-map/problems/49-group-anagrams.md) | [`💻 49-group-anagrams.py`](./05-hashmap-frequency-map/problems/49-group-anagrams.py) | Canonical Key Hash Map | Use tuple(sorted(word)) or character count tuple as dictionary key | $O(n * k log k)$ | $O(n * k)$ |
| 560 | [`📄 LC 560: Subarray Sum Equals K`](./05-hashmap-frequency-map/problems/560-subarray-sum-equals-k.md) | [`💻 560-subarray-sum-equals-k.py`](./05-hashmap-frequency-map/problems/560-subarray-sum-equals-k.py) | Prefix Sum + HashMap | Count previous occurrences of prefix_sum - k in map initialized with {0: 1} | $O(n)$ | $O(n)$ |

---

## 07. Monotonic Stack

> **Pattern Folder:** [📂 `06-monotonic-stack`](./06-monotonic-stack/README.md) | **Implemented Solutions:** 6 Problems

### 💡 Mental Model & Intuition
A waiting room of **unresolved elements**.
- **Monotonic Decreasing Stack**: Looking for the **Next Greater Element**. Elements sit in the stack in descending order. When a larger number arrives, it **resolves and evicts** everyone shorter than it.
- **Monotonic Increasing Stack**: Looking for the **Next Smaller Element** (used to bound rectangle widths in histograms).
- **The Pop Moment Invariant**: Every answer is computed **at the moment an element is popped** from the stack.

```text
Processing Array: [ 2, 1, 5, 3, 6 ]
Step 1: Push index 0 (val 2) -> Stack: [2]
Step 2: Push index 1 (val 1) -> Stack: [2, 1]
Step 3 (val 5 arrives):
  5 > 1 -> Pop 1! (Answer for 1 is 5)
  5 > 2 -> Pop 2! (Answer for 2 is 5)
  Push 5 -> Stack: [5]
```

### 🚨 When to Use
- Next/Previous greater or smaller element.
- How many days until warmer temperature.
- Histogram max rectangle or stock span.
- Maximum value in sliding window of size $k$ (Monotonic Deque).

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Next Greater Element / Daily Temperatures (Index Stack)
```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []  # Stores indices of unresolved days
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx  # Days waited
        stack.append(i)
    return res
```

#### Template 2: Next Greater Element II (Circular Array — 2 Passes)
```python
def next_greater_elements_circular(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        idx = i % n
        while stack and nums[stack[-1]] < nums[idx]:
            prev_idx = stack.pop()
            res[prev_idx] = nums[idx]
        if i < n:
            stack.append(idx)
    return res
```

#### Template 3: Largest Rectangle in Histogram (O(n))
```python
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # (index, height)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx  # Extend current bar leftward to popped bar's start
        stack.append((start, h))
        
    # Flush remaining bars extending to the right end
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area
```

#### Template 4: Sliding Window Maximum (Monotonic Deque)
```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    q = deque()  # Stores indices, maintains monotonic decreasing values
    res = []
    for i, x in enumerate(nums):
        # 1. Pop smaller elements from back
        while q and nums[q[-1]] < x:
            q.pop()
        q.append(i)
        
        # 2. Evict out-of-window elements from front
        if q[0] < i - k + 1:
            q.popleft()
            
        # 3. Append max to result once first window is formed
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

### ⚠️ Edge Cases & Invariants
- **Store Indices, Not Values**: Always store indices in the stack so you can compute distances (`i - popped_idx`) and access original values.
- **Pop Moment**: The popped item is resolved *by* the current item entering.
- **Monotonic Deque Front**: The front of a monotonic decreasing deque is always the maximum element in the active window.

---

### 📚 Problem Catalog & Code Links (6 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 239 | [`📄 LC 239: Sliding Window Maximum`](./06-monotonic-stack/problems/239-sliding-window-maximum.md) | [`💻 239-sliding-window-maximum.py`](./06-monotonic-stack/problems/239-sliding-window-maximum.py) | Monotonic Decreasing Deque | Deque front always holds max element index; evict old indices from front | $O(n)$ | $O(k)$ |
| 496 | [`📄 LC 496: Next Greater Element I`](./06-monotonic-stack/problems/496-next-greater-element-i.md) | [`💻 496-next-greater-element-i.py`](./06-monotonic-stack/problems/496-next-greater-element-i.py) | Monotonic Decreasing Stack | Maintain decreasing stack; store mapping val -> next_greater on pop | $O(n + m)$ | $O(n)$ |
| 503 | [`📄 LC 503: Next Greater Element II`](./06-monotonic-stack/problems/503-next-greater-element-ii.md) | [`💻 503-next-greater-element-ii.py`](./06-monotonic-stack/problems/503-next-greater-element-ii.py) | Circular Monotonic Stack | Loop twice (2n) with index modulo n to simulate circular array | $O(n)$ | $O(n)$ |
| 739 | [`📄 LC 739: Daily Temperatures`](./06-monotonic-stack/problems/739-daily-temperatures.md) | [`💻 739-daily-temperatures.py`](./06-monotonic-stack/problems/739-daily-temperatures.py) | Monotonic Decreasing Index Stack | Store day indices; when warmer day arrives, pop and record curr_i - popped_i | $O(n)$ | $O(n)$ |
| 84 | [`📄 LC 84: Largest Rectangle in Histogram`](./06-monotonic-stack/problems/84-largest-rectangle-in-histogram.md) | [`💻 84-largest-rectangle-in-histogram.py`](./06-monotonic-stack/problems/84-largest-rectangle-in-histogram.py) | Monotonic Increasing Stack | Popping a taller bar means its right boundary is i and left is stack top; calculate area | $O(n)$ | $O(n)$ |
| 901 | [`📄 LC 901: Online Stock Span`](./06-monotonic-stack/problems/901-online-stock-span.md) | [`💻 901-online-stock-span.py`](./06-monotonic-stack/problems/901-online-stock-span.py) | Monotonic Stack Pair | Stack stores (price, span); accumulate spans of popped smaller prices | $O(1) amortized$ | $O(n)$ |

---

## 08. BFS / Level Order Traversal

> **Pattern Folder:** [📂 `07-bfs-level-order`](./07-bfs-level-order/README.md) | **Implemented Solutions:** 9 Problems

### 💡 Mental Model & Intuition
Ripples expanding outwards from a stone dropped in water.
- **Shortest Path Guarantee**: Because a FIFO queue visits all nodes at distance $d$ before any node at distance $d+1$, the first time BFS reaches a target, that path is guaranteed to be the shortest.
- **The 'Known Answers at $t=0$' Rule (Multi-Source BFS)**:
  - *Rotting Oranges*: Seed all rotten oranges at $t=0$.
  - *01 Matrix*: Seed all `0` cells at distance $0$.
  - *Map of Highest Peak*: Seed all water cells at height $0$.

```text
Tree Level Order:
Level 0:        [ 1 ]
               /     \\
Level 1:    [ 2 ]   [ 3 ]
            /   \\       \\
Level 2:  [ 4 ] [ 5 ]   [ 6 ]
```

### 🚨 When to Use
- Shortest path in unweighted graphs or grids.
- Binary tree level-order, zigzag, or right-side view.
- Simultaneous multi-point spreading (Rotting Oranges, Flood Fill, Infection models).

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Level-Order Tree Traversal (Snapshot level_size)
```python
from collections import deque

def level_order(root):
    if not root: return []
    q = deque([root])
    levels = []
    while q:
        level_size = len(q)  # Snapshot current ripple size
        curr_level = []
        for _ in range(level_size):
            node = q.popleft()
            curr_level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(curr_level)
    return levels
```

#### Template 2: Multi-Source Grid BFS
```python
from collections import deque

def multi_source_grid_bfs(grid: list[list[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    # 1. Seed all known sources at t=0
    for r in range(ROWS):
        for c in range(COLS):
            if is_source(grid[r][c]):
                q.append((r, c, 0))  # (row, col, distance)
                
    # 2. Expand ripples outward
    max_dist = 0
    visited = set(q)
    while q:
        r, c, d = q.popleft()
        max_dist = max(max_dist, d)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, d + 1))
    return max_dist
```

### ⚠️ Edge Cases & Invariants
- **Enqueue-Time Visited Marking**: ALWAYS mark nodes as visited at the moment they are pushed into the queue, never when popped.
- **Level-Size Snapshot**: Take `level_size = len(q)` at the top of the outer while loop to separate discrete graph levels cleanly.

---

### 📚 Problem Catalog & Code Links (9 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 102 | [`📄 LC 102: Binary Tree Level Order Traversal`](./07-bfs-level-order/problems/102-binary-tree-level-order-traversal.md) | [`💻 102-binary-tree-level-order-traversal.py`](./07-bfs-level-order/problems/102-binary-tree-level-order-traversal.py) | Level Snapshot BFS | Snapshot len(q) to process nodes in exact discrete tiers | $O(n)$ | $O(n)$ |
| 103 | [`📄 LC 103: Binary Tree Zigzag Level Order Traversal`](./07-bfs-level-order/problems/103-binary-tree-zigzag-level-order-traversal.md) | [`💻 103-binary-tree-zigzag-level-order-traversal.py`](./07-bfs-level-order/problems/103-binary-tree-zigzag-level-order-traversal.py) | Alternating Level Snapshot BFS | Maintain boolean flag left_to_right; reverse level list when False | $O(n)$ | $O(n)$ |
| 127 | [`📄 LC 127: Word Ladder`](./07-bfs-level-order/problems/127-word-ladder.md) | [`💻 127-word-ladder.py`](./07-bfs-level-order/problems/127-word-ladder.py) | Generic State BFS | Build wildcard intermediate map h*t -> [hot, hit]; BFS gives shortest mutation | $O(M^2 * N)$ | $O(M^2 * N)$ |
| 1765 | [`📄 LC 1765: Map of Highest Peak`](./07-bfs-level-order/problems/1765-map-of-highest-peak.md) | [`💻 1765-map-of-highest-peak.py`](./07-bfs-level-order/problems/1765-map-of-highest-peak.py) | Multi-Source BFS | Seed all water cells at height 0; each adjacent land cell is curr_height + 1 | $O(m * n)$ | $O(m * n)$ |
| 199 | [`📄 LC 199: Binary Tree Right Side View`](./07-bfs-level-order/problems/199-binary-tree-right-side-view.md) | [`💻 199-binary-tree-right-side-view.py`](./07-bfs-level-order/problems/199-binary-tree-right-side-view.py) | Level-Order Last Node BFS | In each level snapshot, record the last element curr_level[-1] | $O(n)$ | $O(n)$ |
| 433 | [`📄 LC 433: Minimum Genetic Mutation`](./07-bfs-level-order/problems/433-minimum-genetic-mutation.md) | [`💻 433-minimum-genetic-mutation.py`](./07-bfs-level-order/problems/433-minimum-genetic-mutation.py) | Shortest Mutation Path BFS | Mutate each gene char with [A, C, G, T]; BFS finds min steps | $O(N * L * 4)$ | $O(N)$ |
| 542 | [`📄 LC 542: 01 Matrix`](./07-bfs-level-order/problems/542-01-matrix.md) | [`💻 542-01-matrix.py`](./07-bfs-level-order/problems/542-01-matrix.py) | Multi-Source BFS | Start from all 0s simultaneously to compute distance to nearest 0 in one pass | $O(m * n)$ | $O(m * n)$ |
| 637 | [`📄 LC 637: Average of Levels in Binary Tree`](./07-bfs-level-order/problems/637-average-of-levels-in-binary-tree.md) | [`💻 637-average-of-levels-in-binary-tree.py`](./07-bfs-level-order/problems/637-average-of-levels-in-binary-tree.py) | Level-Order Aggregation BFS | Sum level elements and divide by level_size | $O(n)$ | $O(n)$ |
| 994 | [`📄 LC 994: Rotting Oranges`](./07-bfs-level-order/problems/994-rotting-oranges.md) | [`💻 994-rotting-oranges.py`](./07-bfs-level-order/problems/994-rotting-oranges.py) | Multi-Source BFS | Seed all rotten oranges at t=0; track fresh orange count to verify total rot | $O(m * n)$ | $O(m * n)$ |

---

## 09. DFS / Backtracking

> **Pattern Folder:** [📂 `08-dfs-backtracking`](./08-dfs-backtracking/README.md) | **Implemented Solutions:** 4 Problems

### 💡 Mental Model & Intuition
1. **Tree DFS (Postorder / Bottom-Up)**: Children solve their subtrees first and report answers upwards to parent nodes (computing subtree height, tree diameter, subtree balance).
2. **Backtracking (Maze Exploration)**:
   - Make a choice (step forward).
   - Recurse deeper.
   - **Undo the choice (backtrack)** so other paths can be explored cleanly.
   - The Call Stack *is* the maze.

```text
Decision Tree Backtracking (Subsets):
              []
         /    |    \\
       [1]   [2]   [3]
       / \\    |
   [1,2][1,3][2,3]
     |
  [1,2,3]
```

### 🚨 When to Use
- Tree properties (height, diameter, balanced tree, path sums).
- Generating ALL permutations, combinations, subsets, or board configurations (N-Queens, Sudoku).
- Grid search with visit backtracking (Word Search).

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Bottom-Up Tree DFS (Diameter / Height)
```python
def diameter_of_binary_tree(root) -> int:
    max_diameter = 0
    def height(node):
        nonlocal max_diameter
        if not node: return 0
        left_h = height(node.left)
        right_h = height(node.right)
        max_diameter = max(max_diameter, left_h + right_h)  # Update longest path
        return 1 + max(left_h, right_h)                     # Return subtree height
    height(root)
    return max_diameter
```

#### Template 2: Universal Backtracking Framework (Subsets / Combinations)
```python
def backtrack_subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def backtrack(start: int, current: list[int]):
        res.append(current[:])  # Collect copy of current state
        for i in range(start, len(nums)):
            current.append(nums[i])      # 1. Choice
            backtrack(i + 1, current)    # 2. Recurse
            current.pop()                # 3. Undo (Backtrack)
    backtrack(0, [])
    return res
```

### ⚠️ Edge Cases & Invariants
- **Always Copy State**: `res.append(current[:])` creates a snapshot copy; appending `current` directly appends a mutating reference.
- **Postorder Aggregation**: For tree properties dependent on child subtrees, compute left and right first before resolving parent.

---

### 📚 Problem Catalog & Code Links (4 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 104 | [`📄 LC 104: Maximum Depth of Binary Tree`](./08-dfs-backtracking/problems/104-maximum-depth-of-binary-tree.md) | [`💻 104-maximum-depth-of-binary-tree.py`](./08-dfs-backtracking/problems/104-maximum-depth-of-binary-tree.py) | Bottom-Up Postorder DFS | height = 1 + max(dfs(left), dfs(right)) | $O(n)$ | $O(h)$ |
| 110 | [`📄 LC 110: Balanced Binary Tree`](./08-dfs-backtracking/problems/110-balanced-binary-tree.md) | [`💻 110-balanced-binary-tree.py`](./08-dfs-backtracking/problems/110-balanced-binary-tree.py) | Bottom-Up Early Exit DFS | Return -1 immediately if any child is unbalanced or |h_L - h_R| > 1 | $O(n)$ | $O(h)$ |
| 112 | [`📄 LC 112: Path Sum`](./08-dfs-backtracking/problems/112-path-sum.md) | [`💻 112-path-sum.py`](./08-dfs-backtracking/problems/112-path-sum.py) | Top-Down Preorder DFS | Subtract node.val at each step; check if leaf node matches target_sum == 0 | $O(n)$ | $O(h)$ |
| 543 | [`📄 LC 543: Diameter of Binary Tree`](./08-dfs-backtracking/problems/543-diameter-of-binary-tree.md) | [`💻 543-diameter-of-binary-tree.py`](./08-dfs-backtracking/problems/543-diameter-of-binary-tree.py) | Bottom-Up Longest Path DFS | Longest path through node is left_h + right_h; update global max | $O(n)$ | $O(h)$ |

---

## 10. Dynamic Programming

> **Pattern Folder:** [📂 `09-dynamic-programming`](./09-dynamic-programming/README.md) | **Implemented Solutions:** 1 Problems

### 💡 Mental Model & Intuition
DP is solving a big problem by breaking it into overlapping subproblems with optimal substructure — and remembering the answers so no calculation is ever repeated.
- **Kadane's Algorithm (1D Local vs Global State)**: At each number $x$, you face a choice:
  1. *Extend* the existing subarray: `curr_sum + x`
  2. *Start fresh* from $x$: `x`
  $$\\text{curr_max} = \\max(x, \\text{curr_max} + x)$$

```text
Kadane's Decision at index i:
               [ ... Subarray ... ]  +  [ nums[i] ]  (Extend)
                                vs
                                        [ nums[i] ]  (Start Fresh)
```

### 🚨 When to Use
- Optimization problems (min cost, max profit, longest sequence).
- Counting combinations / distinct ways to reach a state.
- Problem displays overlapping subproblems and optimal substructure.

---

### 🛠️ Sub-Pattern Code Templates

#### Template 1: Kadane's Algorithm (O(1) Space DP)
```python
def max_sub_array(nums: list[int]) -> int:
    curr_sum = max_sum = nums[0]
    for x in nums[1:]:
        curr_sum = max(x, curr_sum + x)  # Either extend or start fresh
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

#### Template 2: 1D Linear Tabulation (Climbing Stairs / House Robber)
```python
def dp_1d(nums: list[int]) -> int:
    if not nums: return 0
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = nums[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[n]
```

### ⚠️ Edge Cases & Invariants
- **Local vs. Global Invariant**: `curr_sum` tracks the best subarray ending *at the current index*, while `max_sum` tracks the best seen across the entire array.
- **Negative Prefix Drop**: A negative running sum can never contribute positively to any future subarray.

---

### 📚 Problem Catalog & Code Links (1 Problems)

| # | Problem Statement (.md) | Solution Code (.py) | Sub-Pattern / Approach | Key "Aha!" Invariant | Time | Space |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: |
| 53 | [`📄 LC 53: Maximum Subarray`](./09-dynamic-programming/problems/53-maximum-subarray.md) | [`💻 53-maximum-subarray.py`](./09-dynamic-programming/problems/53-maximum-subarray.py) | Kadane 1D Local/Global DP | If running sum becomes negative, it hurts future subarrays — drop it and start fresh at x | $O(n)$ | $O(1)$ |

---

## 🎯 Master Revision Flashcard Self-Quiz

Use these 10 rapid-fire questions to test your active recall before tackling new patterns:

1. **Q:** Why do we move the *shorter* wall in *Container With Most Water*?  
   **A:** Because the area is constrained by the shorter wall. Moving the taller wall reduces width without any chance of increasing the restricting height.
2. **Q:** What is the critical condition for when to use *Sliding Window* vs *Prefix Sum + HashMap* for subarray sums?  
   **A:** If the array has **negative numbers**, sliding window monotonicity breaks (growing window might decrease sum); you MUST use *Prefix Sum + HashMap*. If all numbers are positive, use *Sliding Window*.
3. **Q:** How do you find the exact cycle entrance node in Floyd's Cycle Detection?  
   **A:** After fast and slow collide, reset slow to head, leave fast at meeting point, and advance both 1 step at a time until they collide again.
4. **Q:** What is the difference between a monotonic increasing stack vs monotonic decreasing stack?  
   **A:** Decreasing stack finds the **Next Greater Element** (pops when element is bigger). Increasing stack finds the **Next Smaller Element** (pops when element is smaller).
5. **Q:** Why must you add grid cells to `visited` on *enqueue* rather than *dequeue* in BFS?  
   **A:** Waiting until dequeue allows identical neighbor cells to be added multiple times by different parents, causing exponential memory explosion and TLE.
6. **Q:** How can you find Top-K frequent elements in $O(n)$ time without a Heap?  
   **A:** Use Bucket Sort: index buckets from $0 \dots n$ by frequency, place elements in their frequency bucket, and scan backward from bucket $n$.
7. **Q:** What is the invariant in Kadane's Algorithm?  
   **A:** `curr_sum = max(x, curr_sum + x)`. If `curr_sum` is negative, reset by starting a new subarray at `x`.
8. **Q:** In Dutch National Flag (3-way partition), why don't we increment `mid` when swapping with `high`?  
   **A:** Because the element swapped from `high` is uninspected and could be 0, 1, or 2; `mid` must examine it on the next iteration.
9. **Q:** What is the formula for counting valid subarrays ending at index $R$ in a variable sliding window?  
   **A:** `R - L + 1`.
10. **Q:** When does Binary Search apply to problems that don't give you a sorted array?  
   **A:** Whenever the search/answer space satisfies a monotonic Boolean predicate (`[False, False, ..., True, True]`).

---

## 🚀 Roadmap: Patterns 11 – 16

Here is the exact implementation order for upcoming patterns:

1. **Pattern #10: Greedy (`10-greedy`)** — Making locally optimal choices without looking back (Jump Game, Gas Station).
2. **Pattern #11: Intervals (`11-intervals`)** — Sorting by start/end times + sweep line (Merge Intervals, Non-overlapping Intervals, Meeting Rooms).
3. **Pattern #12: Heap / Priority Queue (`12-heap-priority-queue`)** — Top-K elements, streaming medians, K-way merges.
4. **Pattern #13: Graph Patterns (`13-graph-patterns`)**:
   - Topological Sort (Kahn's In-degree Algorithm & DFS Postorder)
   - Union-Find / Disjoint Set Union (Path Compression & Union by Rank)
   - Dijkstra's Algorithm (Shortest path in positive weighted graphs)
5. **Pattern #14: Trie (`14-trie`)** — Prefix trees, autocomplete, word search dictionary trees.
6. **Pattern #15: Bit Manipulation (`15-bit-manipulation`)** — XOR tricks, bit masking, subset generation.
