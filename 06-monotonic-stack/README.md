# 06 — Monotonic Stack (Deque)

> **Status:** 🔄 In Progress | **Problems Solved:** 1

---

## 📌 Pattern Notes

### 1. What is it?
A regular stack lets you push and pop anything. A **Monotonic Stack (or Monotonic Deque)** is a data structure where elements are always stored in a specific order (either **strictly increasing** or **strictly decreasing**).
**Before you push a new element, you evict anything that violates the order.**

### 2. When do I use it? — The Signals 🚨
The common thread: **"For each element, find the nearest element in a specific direction that satisfies a condition."**
- "Next greater element" / "Next smaller element"
- "Previous greater element" / "Previous smaller element"
- "How many days until warmer temperature"
- "Largest rectangle in histogram"

### 3. The Logic — "Unresolved" Elements
Forget complex analogies. Think of the stack as a **list of unresolved elements**.

1.  **The Stack = Unresolved Elements:** At any moment, the stack holds indices of elements that have *not yet found* their answer (e.g., they haven't found a taller bar to their right).
2.  **New Element Resolves Old Ones:** When a new element arrives, if it is "stronger" (greater/smaller) than the top of the stack, it **resolves** those elements.
3.  **The Pop Moment:** The moment an element is popped, it has found its answer. The answer is the current element that triggered the pop.

#### Visual Logic (Next Greater Element)
Array: `[2, 1, 5, 3, 6]`

- **Step 1 (2):** Stack `[0]` (value 2). Nothing to resolve.
- **Step 2 (1):** Stack `[0, 1]` (values 2, 1). 1 is not taller than 2.
- **Step 3 (5):** 5 is taller than 1! **Pop 1**, `result[1] = 5`. 5 is taller than 2! **Pop 0**, `result[0] = 5`. Stack `[2]` (value 5).
- **Step 4 (3):** Stack `[2, 3]` (values 5, 3).
- **Step 5 (6):** 6 is taller than 3! **Pop 3**, `result[3] = 6`. 6 is taller than 5! **Pop 2**, `result[2] = 6`. Stack `[4]` (value 6).

### 4. Deep Dive: Popping & Result Logic
The core of the algorithm lives in these two lines:
```python
while stack and nums[i] > nums[stack[-1]]:
    idx = stack.pop()       # This element's search is OVER
    result[idx] = nums[i]   # The answer is the element that just arrived
```

- **Why the `while` loop?** One new element can be the answer for *multiple* previous elements (like 5 resolving both 1 and 2).
- **Why `stack.pop()`?** We remove the element because it found its "nearest" match. It doesn't need to look anymore.
- **Why `result[idx] = nums[i]`?** We use the index stored in the stack to record the answer exactly where it belongs in the output array.

### 5. Generalized Rules for Monotonic Stack
Follow this decision tree for any problem:

#### Rule 1: Decide Stack Type
- Looking for **GREATER** element → **DECREASING** stack (pop when `current > top`)
- Looking for **SMALLER** element → **INCREASING** stack (pop when `current < top`)

#### Rule 2: Decide Direction
- **Next** greater/smaller (Right) → Traverse **Left to Right**
- **Previous** greater/smaller (Left) → Traverse **Right to Left**

#### Rule 3: The Template
```python
def solve(nums):
    n = len(nums)
    result = [-1] * n
    stack = [] # Stores INDICES

    for i in range(n):
        # 1. RESOLVE: Pop everything the current element "beats"
        while stack and CONDITION(nums[i], nums[stack[-1]]):
            idx = stack.pop()
            result[idx] = RECORD_LOGIC # value, distance, or area
            
        # 2. ADD: Current element joins the "unresolved" list
        stack.append(i)
        
    return result
```

#### Rule 4: Stack vs Deque
- **Stack:** Used for "nearest greater/smaller" with no range limit.
- **Deque:** Used when there is a **window size (k)**. You must also evict from the front (`popleft`) if `deque[0]` is outside the window: `while deque and deque[0] <= i - k: deque.popleft()`.

---

## 🗂️ LeetCode Practice List

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | [Sliding Window Maximum](./problems/239-sliding-window-maximum.md) | Hard | Monotonic Deque (decreasing) to track max in $O(1)$. |
| 2 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | Pure template. |
| 3 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Record distance: `i - idx`. |
| 4 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | Circular array: loop twice with `i % n`. |
| 5 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Pop triggers area calculation. |
