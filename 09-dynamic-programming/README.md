# Pattern 10: Dynamic Programming

> **Status:** 🔄 In Progress | **Problems Solved:** 1

---

## 1. What is it?
DP is the art of solving a big problem by solving smaller versions of the same problem — and remembering the answers so you never compute the same thing twice.

Two ingredients:
- **Overlapping subproblems** — the same smaller problem keeps appearing.
- **Optimal substructure** — the best answer to the big problem is built from the best answers to the smaller problems.

## 2. When do I use it?
Your brain should scream "DP" when you see any of these signals:

| Signal in the problem | Example phrasing |
| :--- | :--- |
| **Count the number of ways** | "how many ways can you..." |
| **Find min/max of something** | "minimum cost", "maximum profit" |
| **Is it possible / can you reach** | "can you reach the end", "is there a path" |
| **Decision at each step** | "at each step you can do X or Y" |
| **Subsequence / substring** | "longest increasing subsequence" |
| **Partition / split** | "split array into two equal subsets" |

**The dead giveaway:** if a brute force solution involves recursion that recomputes the same inputs repeatedly, you need DP.

## 3. The Mental Model
Imagine you're climbing stairs. You can take 1 or 2 steps at a time. How many ways to reach step 5?
The DP brain says: "To reach step 5, I came from step 4 or step 3. So `ways(5) = ways(4) + ways(3)`. And I already know those."
You build forward using answers you've already stored.

## 4. The Two Flavors of DP

### Flavor 1: Top-Down (Memoization)
Start from the big problem. Recurse down. Cache results so you don't recompute.
- Feels like: natural recursion + a dictionary to remember.
- Good when: the state space is large but you don't visit all states.

### Flavor 2: Bottom-Up (Tabulation)
Start from the smallest subproblem. Fill a table. Work your way up.
- Feels like: filling a spreadsheet from left to right.
- Good when: you visit all states anyway, and you want to avoid recursion overhead.

## 5. The Four-Step DP Framework
Every DP problem you ever see — apply this framework:
- **Step 1:** Define what `dp[i]` MEANS in plain English.
- **Step 2:** Find the RECURRENCE — how `dp[i]` relates to smaller states.
- **Step 3:** Set the BASE CASES — the smallest problems you know the answer to directly.
- **Step 4:** Figure out the ITERATION ORDER — which direction do you fill the table?

## 6. The 1D DP Template
Here is the generalized skeleton for 1D DP:
```python
def dp_1d(input):
    n = len(input)
    dp = [0] * (n + 1)     # or [0] * n, depends on indexing
    
    # --- Base cases ---
    dp[0] = <base_0>
    dp[1] = <base_1>        # if needed
    
    # --- Fill the table ---
    for i in range(2, n + 1):
        dp[i] = <recurrence using dp[i-1], dp[i-2], input[i]>
    
    return dp[n]             # or dp[-1]
```

## 7. The Three Subpatterns of DP
- **1D DP**
  - Linear sequence decisions (Climbing Stairs, House Robber, Coin Change)
  - Subsequence decisions (Longest Increasing Subsequence)
- **2D DP**
  - Two-sequence problems (Longest Common Subsequence, Edit Distance)
  - Grid problems (Unique Paths, Minimum Path Sum)
- **Interval DP**
  - Split/merge subproblems (Burst Balloons, Matrix Chain Multiplication)

---

## 🗂️ Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 53 | [Maximum Subarray](./problems/53-maximum-subarray.md) | Medium | Kadane's Algorithm — The "Standard" DP solution. |
| 70 | Climbing Stairs | Easy | Pure 1D DP baseline. |
| 198 | House Robber | Medium | Binary choice at each step. |
| 746 | Min Cost Climbing Stairs | Easy | Min instead of max/count. |
| 322 | Coin Change | Medium | Unbounded choices, not just 1 or 2. |
| 139 | Word Break | Medium | String DP — is it possible? |
