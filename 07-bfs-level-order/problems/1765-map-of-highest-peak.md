# 1765. Map of Highest Peak

**Difficulty:** Medium

**Link:** [LeetCode 1765](https://leetcode.com/problems/map-of-highest-peak/)

## Problem Description

You are given an integer matrix `isWater` of size `m x n` that represents a map of land and water cells.

- If `isWater[i][j] == 0`, cell `(i, j)` is a land cell.
- If `isWater[i][j] == 1`, cell `(i, j)` is a water cell.

You must assign each cell a height following these rules:
1. The height of each cell must be non-negative.
2. If the cell is a water cell, its height must be `0`.
3. Any two adjacent cells must have an absolute height difference of at most `1`.

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix `height` of size `m x n`.

## Approach: Multi-Source BFS
This problem is identical in logic to "01 Matrix". 

1. **Identify the Sources:** The water cells have a known height of `0`. These are our BFS starting points.
2. **Initialize:** 
   - A `queue` with all water cell coordinates.
   - A `result` matrix where water cells are `0` and land cells are marked as unvisited (e.g., `-1`).
3. **BFS Expansion:** 
   - For each cell in the queue, explore its neighbors.
   - If a neighbor is land and hasn't been assigned a height:
     - Assign `height[neighbor] = height[current] + 1`.
     - Add the neighbor to the queue.

By starting BFS from all water cells simultaneously, we ensure that every land cell is assigned the minimum possible distance to the nearest water, which satisfies the "difference of at most 1" rule while maximizing the overall height.
