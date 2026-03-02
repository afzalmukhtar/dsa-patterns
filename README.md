# 🧠 DSA Patterns — My Personal Learning Journal

> A structured, pattern-first approach to mastering Data Structures & Algorithms.
> Every note, problem, and solution in this repo was learned and written by me — built up one pattern at a time.

---

## 📖 What Is This?

This repository is my personal DSA learning journal. Instead of grinding random LeetCode problems, I'm learning **how to think** by studying **recurring patterns** that show up across hundreds of problems.

Each folder contains:
- **A deep-dive README** — the intuition, mental model, brute force → optimal progression, templates, and edge cases for that pattern
- **Problem files** — the problem statement + my solution for each problem I've solved under that pattern

The goal isn't to memorize solutions. It's to **recognize patterns from first principles** and build solutions systematically.

---

## 🗂️ Pattern Index

| # | Pattern | Core Idea | Typical Complexity |
|---|---------|-----------|-------------------|
| 01 | [Two Pointers](./01-two-pointers/README.md) | Two indices moving toward/away from each other | O(n) time, O(1) space |
| 02 | [Sliding Window](./02-sliding-window/README.md) | A moving subarray/substring of variable or fixed size | O(n) time, O(k) space |
| 03 | [Fast & Slow Pointers](./03-fast-slow-pointers/README.md) | Two pointers at different speeds to detect cycles | O(n) time, O(1) space |
| 04 | [Binary Search](./04-binary-search/README.md) | Eliminate half the search space each step | O(log n) time |
| 05 | [Prefix Sum](./05-prefix-sum/README.md) | Precompute cumulative sums for range queries | O(1) query, O(n) build |
| 06 | [HashMap / Frequency Map](./06-hashmap-frequency-map/README.md) | Trade space for O(1) lookups | O(n) time, O(n) space |
| 07 | [Monotonic Stack](./07-monotonic-stack/README.md) | Maintain a stack that's always sorted | O(n) time, O(n) space |
| 08 | [BFS / Level Order](./08-bfs-level-order/README.md) | Explore layer by layer using a queue | O(V+E) time |
| 09 | [DFS / Backtracking](./09-dfs-backtracking/README.md) | Explore all paths, prune dead ends | O(2^n) worst case |
| 10 | [Dynamic Programming](./10-dynamic-programming/README.md) | Break into subproblems, cache results | Varies |
| 11 | [Greedy](./11-greedy/README.md) | Always pick the locally optimal choice | Usually O(n log n) |
| 12 | [Intervals](./12-intervals/README.md) | Sort + sweep for overlapping ranges | O(n log n) time |
| 13 | [Heap / Priority Queue](./13-heap-priority-queue/README.md) | Always have access to min/max efficiently | O(log n) per op |
| 14 | [Graph Patterns](./14-graph-patterns/README.md) | Union Find, Topo Sort, Dijkstra | O(E log V) |
| 15 | [Trie](./15-trie/README.md) | Prefix tree for string search | O(m) per operation |
| 16 | [Bit Manipulation](./16-bit-manipulation/README.md) | Use binary representation for fast ops | O(1) or O(n) |

---

## 🔁 My Learning Workflow

```
1. Learn the pattern (README in each folder)
       ↓
2. Recognize the signals in a problem statement
       ↓
3. Think through brute force → optimal
       ↓
4. Code the solution
       ↓
5. Push to this repo
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
│       └── 001-two-sum-sorted.py      ← My solution
├── 02-sliding-window/
│   ├── README.md
│   └── problems/
│       └── ...
└── ... (same structure for all 16 patterns)
```

---

## 🧭 How to Use This Repo

- **Learning a new pattern?** → Open the folder's `README.md`
- **Looking at a specific problem?** → Go to `problems/` inside the relevant pattern folder
- **Each `.md` problem file** contains: problem statement, constraints, examples, and my thought process
- **Each `.py` (or `.js`) file** contains: my solution with comments explaining the pattern application

---

## 🛠️ Setup

```bash
git clone https://github.com/YOUR_USERNAME/dsa-patterns.git
cd dsa-patterns
```

No dependencies. Pure thinking. 🧠

---

## 📈 Progress Tracker

| Pattern | Status | Problems Solved |
|---------|--------|----------------|
| Two Pointers | 🔄 In Progress | 0 |
| Sliding Window | ⏳ Not Started | 0 |
| Fast & Slow Pointers | ⏳ Not Started | 0 |
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

*Built with curiosity, not shortcuts. 🚀*
