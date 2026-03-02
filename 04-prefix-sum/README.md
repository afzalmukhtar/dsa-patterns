# 04 — Prefix Sum

> **Status:** 🔄 In Progress | **Problems Solved:** 0

---

## 📌 Pattern Notes

### 1. What is it?
Imagine you have an array of numbers, and someone keeps asking you:
*"What's the sum of elements from index 2 to index 7?"*

The naive way: add them up each time → $O(n)$ per query.
The **Prefix Sum** way: precompute all cumulative sums once, then answer any range query in $O(1)$.

It's a precomputation trick — trade a little space and one upfront pass for lightning-fast range queries later.

### 2. When do I use it? — The Signals 🚨

| Clue in the problem | Why it points to Prefix Sum |
|---|---|
| "sum of subarray from i to j" | Classic range query |
| "number of subarrays with sum = k" | Need cumulative sum + hashmap |
| "find subarray with sum divisible by k" | Modular prefix sums |
| Multiple queries on same array | Precompute once, query many |
| "running total" or "balance at time t" | Prefix sum is a running total |
| 2D grid: "sum of rectangle" | 2D prefix sum |

### 3. The Mental Model
Think of it like a ruler with pre-marked mile markers on a highway:

```text
Highway:   [3,  1,  4,  1,  5,  9,  2,  6]
Miles:      0   3   4   8   9  14  23  25  31
                ^               ^
         start=1            end=5
```
Distance from `1→5` = `miles[6] - miles[1] = 23 - 3 = 20`.
You don't re-drive the road each time. You just subtract two markers.

### 4. Brute Force First
**Problem:** Given array `nums`, answer `Q` queries: "what's the sum from index `L` to `R`?"

```python
# O(n) per query → O(n * Q) total — terrible for many queries
def range_sum_brute(nums, L, R):
    total = 0
    for i in range(L, R + 1):
        total += nums[i]
    return total
```
For 1000 queries on a 10,000 element array → **10 million operations**. 😬

### 5. The "Aha" Insight 💡
> **Sum from L to R = (sum from 0 to R) − (sum from 0 to L−1)**

If you precompute all prefix sums: `prefix[i] = nums[0] + nums[1] + ... + nums[i-1]`
Then: `rangeSum(L, R) = prefix[R+1] - prefix[L]`

You do **$O(n)$ work once**, then every query is **$O(1)$**.

### 6. The Optimal Solution
**Step-by-step visual:**
```text
nums   =  [ 3,  1,  4,  1,  5,  9 ]
index       0   1   2   3   4   5

prefix =  [ 0,  3,  4,  8,  9, 14, 23 ]
index       0   1   2   3   4   5   6
            ^
            always start with 0 (empty prefix)

Query: sum from L=2 to R=4
= prefix[5] - prefix[2]
= 14 - 4
= 10  ✓  (4 + 1 + 5 = 10)
```

**Code:**
```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix, L, R):
    return prefix[R + 1] - prefix[L]
```
**Time:** $O(n)$ to build, $O(1)$ per query | **Space:** $O(n)$ for the prefix array

### 7. The Templates

#### Basic Prefix Sum Template
```python
def solve(nums):
    n = len(nums)
    # Step 1: Build prefix sum (size n+1, prefix[0] = 0)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # Step 2: Answer range query in O(1)
    # sum(L, R) = prefix[R+1] - prefix[L]
    return prefix
```

#### Prefix Sum + HashMap Template (Subarray Sum = k)
```python
from collections import defaultdict

def count_subarrays_with_sum_k(nums, k):
    count = 0
    running_sum = 0
    seen = defaultdict(int)
    seen[0] = 1  # ← CRITICAL: empty prefix has sum 0
    
    for num in nums:
        running_sum += num
        # If (running_sum - k) was seen before,
        # those are valid subarrays ending here
        count += seen[running_sum - k]
        seen[running_sum] += 1
    
    return count
```

### 8. Variations & Edge Cases

- **Negative numbers:** Unlike sliding window, prefix sum + hashmap handles negatives perfectly because it's just arithmetic subtraction.
- **Subarray sum divisible by k:** Instead of `seen[sum - k]`, track `seen[sum % k]`. Two prefix sums with the same remainder mean the subarray between them is divisible by k.
- **In-place Prefix Sum:** If you can't use extra space and are allowed to modify the input:
  ```python
  for i in range(1, len(nums)):
      nums[i] += nums[i-1]
  ```

---

## 🕵️ Deep Dive: The Subarray Sum Equals K Trick

> **❓ Common Doubt:** *"I did not understand the math for Prefix Sum + HashMap. If `prefix[i] - prefix[j] = k`, does that mean if `prefix[j]` exists, there is 100% a subarray present that has the sum equal to k?"*

Yes! You've understood it perfectly. We want a subarray from `j → i` with sum = `k`.

In prefix sum language, that means:
`prefix[i] - prefix[j] = k`

Rearrange:
`prefix[j] = prefix[i] - k`

So as we walk through the array computing `prefix[i]` (which is `running_sum` in the code), we just ask:
*"Has the value `running_sum - k` ever appeared as a prefix sum before?"*
If yes → there exists some index `j` where that prefix sum lived → the subarray from `j` to `i` has sum exactly `k`.

**Visual trace:**
`nums = [1, 2, 1, 3], k = 3`
```text
prefix array: [0, 1, 3, 4, 7]
               ^
            seen={0:1} initialized here

num=1: sum=1, need seen[1-3]=-2 → nope. seen={0:1, 1:1}
num=2: sum=3, need seen[3-3]=0  → seen[0]=1 → count=1 🎯 (subarray [1,2])
num=1: sum=4, need seen[4-3]=1  → seen[1]=1 → count=2 🎯 (subarray [2,1])
num=3: sum=7, need seen[7-3]=4  → seen[4]=1 → count=3 🎯 (subarray [3])

Answer: 3 subarrays → [1,2], [2,1], [3] ✓
```

**The tricky part — why `seen[0] = 1`?**
This handles the case where `running_sum` itself equals `k` — meaning the subarray starts from index 0. Without `seen[0] = 1`, you'd miss every valid subarray that starts at the beginning!

---

## 🗺️ Deep Dive: 2D Prefix Sum Explained Visually

> **❓ Common Doubt:** *"Explain 2D array prefix sum to me. I'm finding it hard to grasp how to build it and query it."*

In 1D, `prefix[i]` = sum of everything to the left of `i`.
In 2D, `prefix[r][c]` = sum of the entire rectangle from the top-left corner `(0,0)` down to cell `(r-1, c-1)`. Think of it like water filling from the top-left corner of the grid into a box.

### Step 1 — Building the 2D Prefix
Original Matrix:
```text
1  2  3
4  5  6
7  8  9
```

`prefix[2][2]` is the sum of this shaded box:
```text
+--+--+
|1 |2 |
+--+--+
|4 |5 |
+--+--+
= 1+2+4+5 = 12
```

We make a prefix table with an extra row and column of zeros (sentinels):
```text
     c=0  c=1  c=2  c=3
r=0 [  0,   0,   0,   0 ]   ← sentinel row
r=1 [  0,   1,   3,   6 ]
r=2 [  0,   5,  12,  21 ]
r=3 [  0,  12,  27,  45 ]
```

**The Formula to Build It:**
How do you compute each cell without re-adding everything? Look at what we already know when filling `prefix[2][2]`:
- `prefix[1][2] = 3` (top strip)
- `prefix[2][1] = 5` (left strip)

If we do `3 + 5 = 8`. But the answer is `12`. Why? Because cell `(0,0)` (the value 1) got counted in **both** strips. We added it twice.

So: `prefix[2][2] = prefix[1][2] + prefix[2][1] - prefix[1][1] + nums[1][1]`
= 3 + 5 - 1 + 5 = 12 ✓

General Formula:
`prefix[r][c] = nums[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]`

### Step 2 — Querying a Rectangle
*"What's the sum of the bottom-right 2x2 block? (r1=1,c1=1) to (r2=2,c2=2)"*
Values are `5+6+8+9 = 28`.

Start with the full top-left rectangle ending at `(r2,c2)`: `prefix[3][3] = 45`.
Remove what we don't want:
- Remove top strip (above r1): `- prefix[1][3] = 6`
- Remove left strip (left of c1): `- prefix[3][1] = 12`

But again — the top-left corner got removed twice, so add it back:
`+ prefix[1][1] = 1`

`45 - 6 - 12 + 1 = 28` ✓

### The One Mental Model to Remember
- **Build:** `cell + top + left − corner` (corner was added twice)
- **Query:** `full − top − left + corner` (corner was removed twice)

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

> **💡 Practice Strategy:** Here is the curated practice list for Prefix Sum. Do not skip problem #4 (`Subarray Sum Equals K`) — everything in Tier 2 depends on truly owning that one pattern first!

### 🟢 Tier 1 — Core Prefix Sum (Do these first)

| # | Problem | Why |
|---|---------|-----|
| 1 | [Running Sum of 1D Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Literally just building the prefix array. Warmup. |
| 2 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Build prefix once, answer range queries. The textbook problem. |
| 3 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Left sum = right sum. Tests your range query thinking. |

### 🟡 Tier 2 — Prefix Sum + HashMap (Do these second)

| # | Problem | Why |
|---|---------|-----|
| 4 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | The most important one. prefix + hashmap, `seen[0]=1` trick. |
| 5 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Modular prefix sum. Sum divisible by k, length ≥ 2. |
| 6 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Modular prefix sum, count all valid subarrays. |
| 7 | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/) | Rearranges into prefix sum + hashmap pattern. Good pattern recognition test. |

### 🔴 Tier 3 — 2D Prefix Sum (Do these last)

| # | Problem | Why |
|---|---------|-----|
| 8 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | The textbook 2D prefix problem. Build table, answer rectangle queries. |
| 9 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Apply 2D prefix query repeatedly across the matrix. |

---

*Notes and problems will be added here over time.*