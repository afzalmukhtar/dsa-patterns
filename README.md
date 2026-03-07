# 🧠 DSA Patterns — A Structured Learning Guide

> A structured, pattern-first approach to mastering Data Structures & Algorithms.
> This repository is designed to help you build intuition and solve problems systematically, one pattern at a time.

---

## 📖 What Is This?

This repository is a comprehensive guide to learning Data Structures and Algorithms. Instead of grinding random LeetCode problems, this guide focuses on teaching you **how to think** by studying **recurring patterns** that show up across hundreds of problems.

Each folder contains:
- **A deep-dive README** — the intuition, mental model, brute force → optimal progression, templates, and edge cases for that pattern.
- **Problem files** — curated problem statements and clear, well-commented solutions demonstrating the pattern in action.

The goal isn't to memorize solutions. It's to **recognize patterns from first principles** and build solutions systematically.

### 🌟 Bonus: Practice Lists
We have intricately mapped the famous **Blind 75** and **NeetCode 150** problem lists into these 15 patterns, complete with frequent company tags (Meta, Amazon, Google, etc.). Check out the mappings to prioritize your practice:
- [🎯 NeetCode 150 Pattern Mapping](./practice/neetcode150.md)
- [🎯 Blind 75 Pattern Mapping](./practice/blind75.md)

---

## 🗂️ Pattern Index

| # | Pattern | Core Idea | Typical Complexity |
|---|---------|-----------|-------------------|
| 01 | [Two Pointers](./01-two-pointers/README.md) | Two indices moving toward/away from each other | O(n) time, O(1) space |
| 02 | [Sliding Window](./02-sliding-window/README.md) | A moving subarray/substring of variable or fixed size | O(n) time, O(k) space |
| 03 | [Binary Search](./03-binary-search/README.md) | Eliminate half the search space each step | O(log n) time |
| 04 | [Prefix Sum](./04-prefix-sum/README.md) | Precompute cumulative sums for range queries | O(1) query, O(n) build |
| 05 | [HashMap / Frequency Map](./05-hashmap-frequency-map/README.md) | Trade space for O(1) lookups | O(n) time, O(n) space |
| 06 | [Monotonic Stack](./06-monotonic-stack/README.md) | Maintain a stack that's always sorted | O(n) time, O(n) space |
| 07 | [BFS / Level Order](./07-bfs-level-order/README.md) | Explore layer by layer using a queue | O(V+E) time |
| 08 | [DFS / Backtracking](./08-dfs-backtracking/README.md) | Explore all paths, prune dead ends | O(2^n) worst case |
| 09 | [Dynamic Programming](./09-dynamic-programming/README.md) | Break into subproblems, cache results | Varies |
| 10 | [Greedy](./10-greedy/README.md) | Always pick the locally optimal choice | Usually O(n log n) |
| 11 | [Intervals](./11-intervals/README.md) | Sort + sweep for overlapping ranges | O(n log n) time |
| 12 | [Heap / Priority Queue](./12-heap-priority-queue/README.md) | Always have access to min/max efficiently | O(log n) per op |
| 13 | [Graph Patterns](./13-graph-patterns/README.md) | Union Find, Topo Sort, Dijkstra | O(E log V) |
| 14 | [Trie](./14-trie/README.md) | Prefix tree for string search | O(m) per operation |
| 15 | [Bit Manipulation](./15-bit-manipulation/README.md) | Use binary representation for fast ops | O(1) or O(n) |

---

## 🔁 Recommended Learning Workflow

```
1. Learn the pattern (Read the README in each folder)
       ↓
2. Learn to recognize the signals in a problem statement
       ↓
3. Think through the progression: brute force → optimal
       ↓
4. Attempt to code the solution yourself
       ↓
5. Compare with the provided solutions
```

---

## 📁 Folder Structure

```
dsa-patterns/
├── README.md                          ← You are here
├── 01-two-pointers/
│   ├── README.md                      ← Full pattern notes
│   └── problems/
│       ├── 001-two-sum-sorted.md      ← Problem statement
│       └── 001-two-sum-sorted.py      ← Example solution
├── 02-sliding-window/
│   ├── README.md
│   └── problems/
│       ├── 643-maximum-average-subarray-i.md
│       └── 643-maximum-average-subarray-i.py
└── ... (same structure for all 15 patterns)
```

---

## 🧭 How to Use This Repo

- **Learning a new pattern?** → Open the folder's `README.md`.
- **Looking at a specific problem?** → Go to `problems/` inside the relevant pattern folder.
- **Each `.md` problem file** contains: the problem statement, constraints, examples, and the thought process.
- **Each `.py` (or `.js`, `.java`, etc.) file** contains: a solution with comments explaining the application of the pattern.

---

## 🛠️ Setup

```bash
git clone https://github.com/afzalmukhtar/dsa-patterns.git
cd dsa-patterns
```

No external dependencies. Just pure problem-solving. 🧠

---

## 📈 Progress Tracker

| Pattern | Status | Problems Available |
|---------|--------|----------------|
| Two Pointers | 🔄 In Progress | 3 |
| Sliding Window | 🔄 In Progress | 1 |
| Binary Search | ⏳ Not Started | 0 |
| Prefix Sum | ⏳ Not Started | 0 |
| HashMap / Frequency Map | ⏳ Not Started | 0 |
| Monotonic Stack | ⏳ Not Started | 0 |
| BFS / Level Order | ⏳ Not Started | 0 |
| DFS / Backtracking | ⏳ Not Started | 0 |
| Dynamic Programming | ⏳ Not Started | 0 |
| Greedy | ⏳ Not Started | 0 |
| Intervals | ⏳ Not Started | 0 |
| Heap / Priority Queue | ⏳ Not Started | 0 |
| Graph Patterns | ⏳ Not Started | 0 |
| Trie | ⏳ Not Started | 0 |
| Bit Manipulation | ⏳ Not Started | 0 |

---

*Built with curiosity, designed for mastery. 🚀*