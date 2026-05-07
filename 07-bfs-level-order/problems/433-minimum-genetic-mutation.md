# 433. Minimum Genetic Mutation

**Difficulty:** Medium

**Link:** [LeetCode 433](https://leetcode.com/problems/minimum-genetic-mutation/)

## Problem Description

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

A mutation is defined as a single character change in the gene string. For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in the `bank` to be considered valid.

Given two gene strings `startGene` and `endGene` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `startGene` to `endGene`. If there is no such mutation, return `-1`.

## Approach: BFS (Shortest Path in Unweighted Graph)

This is a classic "Shortest Path" problem where:
- **Nodes:** Valid gene strings (from the bank).
- **Edges:** A mutation (1-character difference) between two valid gene strings.
- **Weight:** Each edge has a weight of 1.

1. **Edge Case:** If `endGene` is not in the `bank`, it's impossible to reach, so return `-1`.
2. **Setup:**
   - Convert the `bank` to a set for $O(1)$ lookups.
   - Use a `queue` for BFS, starting with `startGene`.
   - Use a `visited` set to avoid cycles and redundant processing.
3. **BFS Traversal:**
   - Process the queue level by level (each level represents one mutation).
   - For each gene, try changing each of its 8 characters to `'A'`, `'C'`, `'G'`, or `'T'`.
   - If the new gene matches `endGene`, return the current mutation count.
   - If the new gene is in the `bank` and hasn't been visited, add it to the queue and mark it as visited.
4. **Return -1** if the queue becomes empty and `endGene` hasn't been reached.
