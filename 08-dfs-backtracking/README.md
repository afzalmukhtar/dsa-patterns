# Pattern 9: DFS / Backtracking

> **Status:** 🏗️ In Progress | **Problems Solved:** 4

---

## 1. What Is It?
Backtracking is systematic trial and error on a decision tree.

At every step, you:
1. Make a choice (add an element, place a character, take a path)
2. Recurse deeper with that choice
3. Undo the choice and try the next option

The "backtrack" is literally step 3 — you undo your last decision and try something else.

## 2. When Do I Use It?
Look for these signals in a problem:
- "find ALL combinations / subsets / permutations"
- "generate all valid ____"
- "find all paths"
- "is there any way to arrange / place / partition"
- "constraint satisfaction" (N-Queens, Sudoku)

**The keyword is ALL.** If a problem asks for every possible arrangement, selection, or path — backtracking.

## 3. The Mental Model
Imagine you're exploring a maze:
```text
        START
          |
    ┌─────┴─────┐
   [A]         [B]       ← you pick a door
    |            |
  ┌─┴─┐        ┌─┴─┐
 [C] [D]      [E] [F]
  |
DEAD END ← come back up, try [D]
```
You go as deep as you can. Hit a wall (base case or invalid state)? Back up one level, try the next door.
The call stack IS the maze. Returning from a function = walking back out of a corridor.

## 4. Brute Force First — Why It's Slow
If you use nested loops for every possible length, it breaks immediately — you need N nested loops for N elements.
The real problem: you don't know depth at compile time. The input size determines how deep you go.

## 5. The "Aha" Moment
Think about each element. You have exactly two choices for each one: include it OR skip it. This forms a binary decision tree.
But in practice, we use a cleaner framing:
"At each step, I pick the NEXT element to add. I use a start index to avoid going backward."

## 6. The Optimal Solution — Subsets
`arr = [1, 2, 3]`

Decision tree with start index:
```text
              []                 ← collect []
         /    |    \
       [1]   [2]   [3]          ← collect each
       / \    |
   [1,2][1,3][2,3]              ← collect each
     |
  [1,2,3]                       ← collect
```

## 7. The Universal Template
This is the skeleton you'll reuse for every backtracking problem:

```python
def backtrack(start, current):
    # ── BASE CASE ──────────────────────────────
    # Either: collect result here (subsets style)
    # Or: check if current is a complete valid solution
    result.append(current[:])   # copy, not reference!

    # ── EXPLORE CHOICES ────────────────────────
    for i in range(start, len(nums)):

        # 1. MAKE A CHOICE
        current.append(nums[i])

        # 2. RECURSE (go deeper)
        backtrack(i + 1, current)

        # 3. UNDO THE CHOICE (backtrack)
        current.pop()
```
The three-line rhythm inside the loop — add → recurse → remove — is the heartbeat of every backtracking solution.

## 8. The Three Flavors of Backtracking
Most problems fall into one of three shapes:

| Problem Type | What changes | Example |
| :--- | :--- | :--- |
| **Subsets** | Collect at every node, use start idx | `[1,2,3]` → all subsets |
| **Permutations** | Collect at leaves, use `visited[]` not start idx | `[1,2,3]` → all orderings |
| **Constraint Satisfaction** | Collect at leaves, prune invalid states early | N-Queens, Sudoku |

## 9. Variations and Edge Cases
- **Duplicates exist? (e.g., `[1, 1, 2]`)**
  Sort first, then skip duplicate elements at the same recursion level:
  ```python
  if i > start and nums[i] == nums[i-1]: continue
  ```
- **Reuse elements? (Combination Sum)**
  Use `backtrack(i, ...)` instead of `backtrack(i + 1, ...)`.
- **Order matters? (Permutations)**
  Don't use `start`. Use a `used[]` boolean array instead, and loop from index `0` every time.
- **Pruning:**
  If you know a branch can't lead to a valid solution, don't go down it: `if current_sum > target: return`. Pruning is what separates a slow backtracker from a fast one.

---

## 🗂️ Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 104 | [Maximum Depth of Binary Tree](problems/104-maximum-depth-of-binary-tree.md) | Easy | Recursive DFS height calculation |
| 112 | [Path Sum](problems/112-path-sum.md) | Easy | Recursive DFS with target reduction |
| 543 | [Diameter of Binary Tree](problems/543-diameter-of-binary-tree.md) | Easy | Longest path via bottom-up DFS height calculation |
| 110 | [Balanced Binary Tree](problems/110-balanced-binary-tree.md) | Easy | Optimized bottom-up balance check |
| 78 | Subsets | Easy | Collect at every node, no constraints |
| 90 | Subsets II | Easy | Input has duplicates. Deduplicate. |
| 77 | Combinations | Medium | Find all k-sized subsets. |
| 39 | Combination Sum | Medium | Same element can be reused. |
| 46 | Permutations | Medium | Order matters. |
| 79 | Word Search | Medium | Backtracking on a 2D grid. |
| 51 | N-Queens | Hard | Constraint satisfaction. |
