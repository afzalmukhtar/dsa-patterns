# 542. 01 Matrix

**Difficulty:** Medium

**Link:** [LeetCode 542](https://leetcode.com/problems/01-matrix/)

## Problem Description

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

The distance between two cells sharing a common edge is `1`.

### Example 1:
**Input:** `mat = [[0,0,0],[0,1,0],[0,0,0]]`
**Output:** `[[0,0,0],[0,1,0],[0,0,0]]`

### Example 2:
**Input:** `mat = [[0,0,0],[0,1,0],[1,1,1]]`
**Output:** `[[0,0,0],[0,1,0],[1,2,1]]`

## Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.

## Approach: Multi-Source BFS
1. Initialize a queue with all the coordinates of cells containing `0`. These are our "sources."
2. Create a `result` matrix of the same size, initialized to `0`.
3. Use a `visited` set (or modify the input matrix to keep track of visited cells) to avoid re-processing.
4. Perform a level-order BFS. For each level, increment the distance.
5. For each cell in the current level, explore its neighbors. If a neighbor is a `1` and hasn't been visited:
   - Set its distance in the `result` matrix.
   - Mark it as visited (or change it to `0` in the input matrix).
   - Add it to the queue for the next level.
