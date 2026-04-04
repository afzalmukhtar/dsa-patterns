# Pattern #7: Monotonic Stack

> **Status:** 🔄 In Progress | **Solved:** 1

---

## 1. What is it?
A regular stack lets you push and pop anything. A **Monotonic Stack** has one extra rule: **Before you push a new element, you evict anything that violates the order.**

The stack stays either always-increasing or always-decreasing from bottom to top. It is a list of **unresolved elements** waiting for their "answer."

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

## 7. The Template & Generalized Rules

### The Core Template
```python
def solve(nums):
    n = len(nums)
    result = [-1] * n
    stack = [] # Stores INDICES

    for i in range(n):
        # 1. RESOLVE: Pop everything the current element "beats"
        while stack and CONDITION(nums[i], nums[stack[-1]]):
            idx = stack.pop()
            result[idx] = WHAT_TO_RECORD
            
        # 2. ADD: Current element joins the "unresolved" list
        stack.append(i)
    return result
```

### The Generalized Rulebook
- **Rule 1 (Signal):** "Find nearest greater/smaller" -> Monotonic Stack.
- **Rule 2 (Type):**
  - Looking for **GREATER** -> **DECREASING** stack (pop when `curr > top`)
  - Looking for **SMALLER** -> **INCREASING** stack (pop when `curr < top`)
- **Rule 3 (Direction):**
  - **Next** (Right) -> Traverse **L to R**
  - **Previous** (Left) -> Traverse **R to L**
- **Rule 4 (Recording):**
  - "Next greater value" -> `res[idx] = nums[i]`
  - "Distance" -> `res[idx] = i - idx`
- **Rule 5 (Deque):** Use if there is a **window size constraint**. Evict from front if `deque[0] < i - k + 1`.

## 8. Variations and Edge Cases
- **Circular Array:** Loop twice (`for i in range(2*n)`) and use `i % n`.
- **Duplicates:** Decide if "greater" includes "equal" (`>=` vs `>`).
- **Stream:** If data arrives one-by-one, the stack naturally handles it.
- **No Extra Space:** Usually not possible as the stack is essential for $O(n)$.

## 9. Practice Problems
1. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) — Easy (Pure Template)
2. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — Medium (Distance Recording)
3. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) — Medium (Circular Array)
4. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) — Hard (Pop triggers area calculation)
