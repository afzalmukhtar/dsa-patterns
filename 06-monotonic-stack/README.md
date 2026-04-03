# 06 — Monotonic Stack (Deque)

> **Status:** 🔄 In Progress | **Problems Solved:** 1

---

## 📌 Pattern Notes

### 1. What is it?
A regular stack lets you push and pop anything. A **Monotonic Stack (or Monotonic Deque)** is a data structure where elements are always stored in a specific order (either **strictly increasing** or **strictly decreasing**).
**Before you push a new element, you evict anything that violates the order.**

That's it. The stack stays either always-increasing or always-decreasing from bottom to top.

| Monotonic Increasing Stack (bottom → top) | Monotonic Decreasing Stack (bottom → top) |
| :--- | :--- |
| `[ 2, 5, 7, 9 ]` ✅ | `[ 9, 7, 5, 2 ]` ✅ |
| `[ 2, 5, 3, 9 ]` ❌ | `[ 9, 5, 7, 2 ]` ❌ |

### 2. When do I use it? — The Signals 🚨
The signal phrases in a problem that scream monotonic stack:
- "Next greater element"
- "Next smaller element"
- "Previous greater element"
- "How many days until warmer temperature"
- "Largest rectangle in histogram"
- "The nearest element that is larger/smaller"
- "For each element, find the first X to its left/right"

**The common thread:** "For each element, find the nearest element in a specific direction that satisfies a condition." If you're ever thinking *"I need to look backward or forward to find the closest thing that's bigger/smaller"* — that's your trigger.

### 3. The Mental Model 🧠
Imagine you're at a concert, standing in a row. You want to know: *"Who is the first person taller than me, to my right?"*

- **The naive way:** Every person turns around and scans right until they find someone taller. That's $O(n^2)$.
- **The smart way:** Imagine walking left to right and maintaining a "waiting list" of people who haven't found their answer yet. The moment a new tall person arrives, they resolve the answer for everyone shorter than them on the waiting list.
- That waiting list is the **Monotonic Stack**.

### 4. Brute Force First
**Problem:** Next Greater Element
Given: `[2, 1, 5, 3, 6]`
Output: `[5, 5, 6, 6, -1]`

```python
def next_greater_brute(nums):
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):   # scan everything to the right
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result
```
**Why it's slow:** For every element, you potentially scan all elements to its right.
- **Time:** $O(n^2)$
- **Space:** $O(1)$

### 5. The Optimization Insight — The "Aha" Moment 💡
When you scan right and find a greater element, what do you do with that information? In brute force — nothing. You throw it away and repeat the same scan for the next element.

**The insight:** When element X is the "next greater" for element A, it's also the next greater for every element between them that is smaller than X.

So instead of scanning forward, scan left-to-right and look backward using a stack:
*"I'm processing element X. Are there any unresolved elements behind me that X is the answer to?"*

If X is greater than the top of the stack → pop it, record the answer, repeat. Then push X itself (it's now waiting for its next greater).

### 6. The Optimal Solution — Step by Step
Array: `[2, 1, 5, 3, 6]`
Stack stores indices (so we can fill `result[i]`).

1. **i=0, nums[0]=2:** Stack empty, push 0. Stack: `[0]` (values: `[2]`)
2. **i=1, nums[1]=1:** `1 < 2`, don't pop. push 1. Stack: `[0, 1]` (values: `[2, 1]`)
3. **i=2, nums[2]=5:**
   - `5 > 1` → POP 1, `result[1] = 5`
   - `5 > 2` → POP 0, `result[0] = 5`
   - Stack empty, push 2. Stack: `[2]` (values: `[5]`)
4. **i=3, nums[3]=3:** `3 < 5`, don't pop. push 3. Stack: `[2, 3]` (values: `[5, 3]`)
5. **i=4, nums[4]=6:**
   - `6 > 3` → POP 3, `result[3] = 6`
   - `6 > 5` → POP 2, `result[2] = 6`
   - Stack empty, push 4. Stack: `[4]` (values: `[6]`)

**Final result:** `[5, 5, 6, 6, -1]` ✅
- **Time:** $O(n)$ — every element is pushed once and popped once.
- **Space:** $O(n)$ — the stack.

### 7. The Template
This is the reusable skeleton. Burn this into memory:

```python
def monotonic_stack_template(nums):
    n = len(nums)
    result = [-1] * n      # default: no answer found
    stack = []             # stores INDICES, not values

    for i in range(n):
        # While the current element "resolves" the top of the stack:
        while stack and nums[i] > nums[stack[-1]]:   # ← change > to < for "next smaller"
            idx = stack.pop()
            result[idx] = nums[i]                    # current element is the answer

        stack.append(i)

    return result
```

### 8. Variations and Edge Cases
- **Variation 1: Next Smaller Element:** Just flip the comparison: `while stack and nums[i] < nums[stack[-1]]`
- **Variation 2: Previous Greater Element:** Traverse right to left (or check `stack[-1]` after popping for NGE).
- **Variation 3: Distance instead of value:** Record `i - idx` instead of `nums[i]` (e.g., Daily Temperatures).
- **Variation 4: Circular array:** Process the array twice (`i` from `0` to `2n-1`), use `i % n` to index.
- **Variation 5: Largest Rectangle in Histogram:** Pop when the next bar is shorter. Compute area using the popped bar as height and the distance between the current index and the new stack top as width.

---

## 🗂️ LeetCode Practice List

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | [Sliding Window Maximum](./problems/239-sliding-window-maximum.md) | Hard | Monotonic Deque (decreasing) to track the max in $O(1)$. |
| 2 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | Pure template, no tricks. |
| 3 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Store distance, not value. |
| 4 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | Circular array variant. |
| 5 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Medium | Previous greater, streaming data. |
| 6 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Pop triggers area computation. |

---

> **The Mental Trigger:** "For each element, find the nearest element in one direction satisfying a condition" → Monotonic Stack. Maintain a stack of unresolved elements. Every new element resolves everything it can, then waits its turn.
