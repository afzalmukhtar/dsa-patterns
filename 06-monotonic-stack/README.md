# Pattern #7: Monotonic Stack

> **Status:** 🔄 In Progress | **Solved:** 1

---

## 1. What is it?
The word **Monotonic** simply means "moving in only one direction" — no zig-zagging allowed.
- **Monotonic Increasing:** Never goes down (e.g., `1, 2, 2, 3, 5, 8`)
- **Monotonic Decreasing:** Never goes up (e.g., `10, 8, 5, 5, 3, 1`)

A regular stack lets you push and pop anything. A **Monotonic Stack** has one extra rule: **Before you push a new element, you evict anything that violates the order.** The stack stays strictly "one-way."

It is a list of **unresolved elements** waiting for their "answer."

## 2. When do I use it?
The signal phrases in a problem that scream Monotonic Stack:
- "Next greater/smaller element"
- "Previous greater/smaller element"
- "How many days until warmer temperature"
- "Largest rectangle in histogram"
- **The Trigger:** "For each element, find the nearest element in a specific direction that satisfies a condition."

## 3. The Mental Model
Imagine a row of people at a concert. Each person wants to know: *"Who is the first person taller than me to my right?"*
As you walk left-to-right, you keep a "waiting list" (the stack). When a tall person arrives, they resolve the answer for everyone shorter than them on that list.

```text
Row: [ 2, 1, 5, 3, 6 ]

Step 3 (5 arrives):
5 > 1? YES -> 1 resolved! (pop)
5 > 2? YES -> 2 resolved! (pop)
Stack: [ 5 ]
```

## 4. Brute Force First
For every element, scan all elements to its right until you find a taller one.
```python
def next_greater_brute(nums):
    res = [-1] * len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                res[i] = nums[j]
                break
    return res
```
- **Time:** $O(n^2)$ because of the nested scan.
- **Why it's slow:** We throw away information. If `5` is the answer for `2`, it might also be the answer for `1`. Brute force scans for both separately.

## 5. The Optimization Insight
**"I'm processing element X. Are there any unresolved elements behind me that X is the answer to?"**
When element X is the "next greater" for element A, it's also the next greater for every element between them that is smaller than X. We can resolve multiple past questions in $O(1)$ each.

## 6. The Optimal Solution
We use a stack to store **indices** of unresolved elements. Every element is pushed once and popped once.
- **Time:** $O(n)$
- **Space:** $O(n)$

### Step-by-Step State Trace
Array: `[2, 1, 5, 3, 6]`

```text
i=0 (2): Stack: [0] (val: 2) | Res: [-1, -1, -1, -1, -1]
i=1 (1): 1 < 2. Stack: [0, 1] (val: 2, 1)
i=2 (5): 5 > 1 -> pop(1), Res[1]=5
         5 > 2 -> pop(0), Res[0]=5
         Stack: [2] (val: 5)
i=3 (3): 3 < 5. Stack: [2, 3] (val: 5, 3)
i=4 (6): 6 > 3 -> pop(3), Res[3]=6
         6 > 5 -> pop(2), Res[2]=6
         Stack: [4] (val: 6)
```

## 7. The Generalised Rules for Monotonic Stack

### Rule 1 — Recognise the problem
If the problem asks **"for each element, find the nearest element to the left/right that is greater/smaller"** → Monotonic Stack.

### Rule 2 — Decide the stack type
- Looking for **GREATER** element → Maintain **DECREASING** stack (pop when `current > top`)
- Looking for **SMALLER** element → Maintain **INCREASING** stack (pop when `current < top`)

**Memory trick:** The stack always holds elements that have NOT yet been beaten. So if you're looking for something greater, only smaller elements survive in the stack — hence decreasing.

### Rule 3 — Decide the direction
- **Next** greater/smaller (to the RIGHT) → traverse **LEFT to RIGHT**
- **Prev** greater/smaller (to the LEFT) → traverse **RIGHT to LEFT**

### Rule 4 — The three-step loop. Always.
```python
for i in range(n):
    # STEP 1: Resolve — pop everything the current element beats
    while stack and CONDITION(nums[i], nums[stack[-1]]):
        idx = stack.pop()
        result[idx] = WHAT_YOU_RECORD   # value? distance? area?

    # STEP 2: Add — current element is now unresolved, push it
    stack.append(i)

# STEP 3: Cleanup — anything left in stack has no answer
# (result already initialised to -1, so often nothing to do)
```
These three steps never change. Only two things vary per problem:
1. The **CONDITION** (greater or smaller)
2. The **WHAT_YOU_RECORD** (value, distance, area)

### Rule 5 — Know what to record when you pop
This is where problems differ from each other:
- **"Next greater value"** → `result[idx] = nums[i]`
- **"Days until warmer"** → `result[idx] = i - idx`
- **"Largest rectangle"** → `result[idx] = height * width` (computed on pop)
- **"Previous greater index"** → `result[idx] = stack[-1] if stack else -1`

The pop moment is where the answer lives. Whatever the problem asks for — compute it right there.

### Rule 6 — When to use a Deque instead of a Stack
A deque (double-ended queue) comes in when the problem adds a window size constraint — meaning old elements need to be evicted from the front while new ones are added to the back.
- **Stack** → "find nearest greater/smaller" (no window limit)
- **Deque** → "find greatest/smallest within a window of size k"

The deque stays monotonic the same way, but you also check:
```python
# Evict from FRONT if it's outside the window
while deque and deque[0] < i - k + 1:
    deque.popleft()
```

## 8. The Full Decision Tree
```text
Problem involves "nearest greater/smaller"?
            │
            ▼
      Which direction?
      ┌─────┴──────┐
    Right          Left
  L→R loop       R→L loop
      │
      ▼
  Greater or Smaller?
  ┌────────┴────────┐
Greater           Smaller
Decreasing        Increasing
stack             stack
(pop when >)      (pop when <)
      │
      ▼
  What to record on pop?
  Value / Distance / Area / Index
      │
      ▼
  Window constraint?
  ┌────┴────┐
  No       Yes
Stack     Deque
          (also evict from front)
```

**One-line version to memorise:**
*Push indices. Pop when beaten. Record the answer at pop time. What survives in the stack is always monotone.*

## 9. Practice Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | Pure Template |
| 2 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Record distance: `i - idx` |
| 3 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | Circular Array |
| 4 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Pop triggers area calculation |
| 5 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic Deque variation |
