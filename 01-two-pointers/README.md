# 01 — Two Pointers

> **Status:** 🔄 In Progress | **Problems Solved:** 16

---

## 📌 Pattern Notes

### 1. What is it?
Imagine you're reading a book from both ends at the same time — one finger starts at page 1, another at the last page, and they move toward each other based on some condition.

That's Two Pointers. Instead of checking every possible pair of elements (which is slow), you place two markers in the array and move them intelligently — eliminating large chunks of work with each step.

### 2. When to use it? — The Signals 🚨
Read a problem and ask yourself:

"Am I working with a sorted array (or can I sort it)? Am I looking for a pair, triplet, or subarray that meets some condition?"

The dead giveaways in problem statements:
- "Find two numbers that sum to X"
- "Is this string/array a palindrome?"
- "Remove duplicates in-place"
- "Move all zeros to the end"
- "Find the closest pair"
- "Container with most water"

The key word buried in almost all of them: the array is sorted, or the problem involves comparing elements from opposite ends, or partitioning elements.

### 3. The Mental Model 🧠
Picture a sorted array laid out flat:

```text
[ 1,  3,  5,  7,  9,  11 ]
  ↑                    ↑
 left               right
```
You want two numbers that sum to 12.

`1 + 11 = 12` ✅ Done.

But what if the target was 10?
- `1 + 11 = 12` → too big → move right inward
- `1 + 9 = 10` ✅

What if target was 14?
- `1 + 11 = 12` → too small → move left inward
- `3 + 11 = 14` ✅

The insight: Because the array is sorted, you have a compass. Sum too big? Right pointer moves left. Sum too small? Left pointer moves right. You never need to go backwards — that's what makes it O(n).

### 4. Brute Force First — Why It's Slow 🐢
Problem: Find two numbers in a sorted array that sum to target.

```python
# O(n²) — check every pair
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
```
Why it's slow: You're checking pairs like (1,3), (1,5), (1,7)... even when you already know 1+11 is too big. You're ignoring information the sorted order is giving you for free.

### 5. The Optimization Insight — The "Aha" Moment 💡
Sorted order gives you a decision rule at every step.

When `arr[left] + arr[right]` is:
- **Too big** → the right element is too large. Move `right` left to get a smaller number.
- **Too small** → the left element is too small. Move `left` right to get a larger number.
- **Equal** → found it.

Each step eliminates either everything to the right of `right` or everything to the left of `left`. You never revisit. That's how O(n²) becomes O(n).

### 6. The Optimal Solution
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1       # need bigger sum
        else:
            right -= 1      # need smaller sum

    return []  # no pair found
```
**Time:** O(n) — each pointer moves at most n times 
**Space:** O(1) — no extra data structures

### 7. The Template / Skeleton 🏗️
This is the reusable shell. Most Two Pointer problems fit this shape:

```python
def two_pointer_template(arr):
    left, right = 0, len(arr) - 1  # or left=0, right=1 for same-direction

    while left < right:
        # compute something using arr[left] and arr[right]

        if condition_met:
            # record answer or return
            pass
        elif need_to_increase:
            left += 1
        else:
            right -= 1

    return result
```

There are actually **two flavors:**

```text
Flavor 1 — Opposite ends (most common):
[ . . . . . . . . ]
  ↑               ↑
 left           right
 → converging toward center

Flavor 2 — Same direction (slow/fast or partition):
[ . . . . . . . . ]
  ↑   ↑
slow fast
 → both moving right, different speeds
```

### 8. Variations & Edge Cases — How Problems Twist This 🌀
- **What if the array is unsorted?** Sort it first — O(n log n) preprocessing. Two pointers still gives you O(n) after that. Total: O(n log n). This is usually acceptable.
- **What if there are duplicates?** After finding a valid pair, skip duplicates by moving the pointer past all identical values:
  ```python
  while left < right and arr[left] == arr[left+1]:
      left += 1
  ```
- **What if it's a triplet (3Sum)?** Fix one element with a for loop, run two pointers on the rest. O(n²) total — still better than O(n³) brute force.
- **What if it's a string palindrome check?** Same idea — left starts at 0, right at end. If characters match, move both inward. If they don't, it's not a palindrome.
- **What if negative numbers are included?** The pointer movement logic still works as long as the array is sorted. Negatives don't break anything — the sorted order is what matters.
- **What if I can't use extra space?** Two pointers are inherently O(1) space — this is one of its biggest strengths. Problems that say "in-place" are often hinting at this pattern.
- **What breaks if you use the wrong pattern here?** If you reach for a HashMap on a two-sum problem, you get O(n) time but O(n) space. That's fine sometimes — but if the problem says sorted array or in-place, it's a signal to use two pointers instead. HashMap also doesn't give you the "closest pair" type answers naturally.

---

## 🕵️ Deep Dive: Visualizing Problem Execution

> **❓ Common Doubt:** *"I'm having trouble visualizing how to apply this to specific problems (like moving zeros, removing duplicates, 3Sum, or container water). Can we walk through some examples visually step-by-step? Also, how exactly do 'slow and fast pointers' work and where do we use them?"*

Let's Break Down These Problems, One by One

### Problem A: Move All Zeros to the End
**The Problem Statement**
```text
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Rules:
- Do it IN-PLACE (no new array)
- Keep the non-zero numbers in their original order
```

**Why is this Two Pointers?**
Ask yourself: "Am I partitioning elements into two groups?"
Yes — zeros vs non-zeros. Anytime you're rearranging in-place by some condition, think Two Pointers (same direction flavor).

**The Mental Model**
Think of it like a bouncer at a door:
- `"slow"` pointer = the WRITER — points to where the next non-zero number should be placed
- `"fast"` pointer = the READER — scans everything, looking for non-zero numbers

**Visual Walkthrough**
```text
arr = [0, 1, 0, 3, 12]

slow = 0 (where to write next non-zero)
fast = 0 (scanner)

─────────────────────────────────────
Step 1: fast=0, arr[fast]=0 → it's zero, skip it
                               just move fast forward

[0, 1, 0, 3, 12]
 S
 F
 → arr[fast] is 0, do nothing, fast moves right

─────────────────────────────────────
Step 2: fast=1, arr[fast]=1 → NON-ZERO!
                               write it at slow, move both

[0, 1, 0, 3, 12]
 S  F
 → arr[fast]=1, write 1 at slow position
 
[1, 1, 0, 3, 12]   ← placed 1 at index 0
    S  F            ← both moved forward

─────────────────────────────────────
Step 3: fast=2, arr[fast]=0 → zero, skip

[1, 1, 0, 3, 12]
    S     F
 → do nothing, fast moves

─────────────────────────────────────
Step 4: fast=3, arr[fast]=3 → NON-ZERO!
                               write it at slow

[1, 1, 0, 3, 12]
    S        F
 → write 3 at index 1

[1, 3, 0, 3, 12]   ← placed 3 at index 1
       S     F      ← both moved

─────────────────────────────────────
Step 5: fast=4, arr[fast]=12 → NON-ZERO!

[1, 3, 0, 3, 12]
       S        F
 → write 12 at index 2

[1, 3, 12, 3, 12]
          S       ← slow is now here

─────────────────────────────────────
Step 6: fast has finished scanning.
        Fill everything from slow onward with 0

[1, 3, 12, 0, 0]  ✅
```

**The Code**
```python
def move_zeros(arr):
    slow = 0  # next position to write a non-zero

    # Phase 1: write all non-zeros forward
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1

    # Phase 2: fill the rest with zeros
    while slow < len(arr):
        arr[slow] = 0
        slow += 1
```
**Time:** O(n) | **Space:** O(1)

---

### Problem B: Remove Duplicates In-Place
**The Problem Statement**
```text
Input:  [1, 1, 2, 3, 3, 4]  ← sorted array
Output: [1, 2, 3, 4, _, _]  ← unique values at front
Return: 4                    ← count of unique values

Rules:
- In-place, no new array
- You only care about the first K elements
```

**Why is this Two Pointers?**
Same flavor as Move Zeros — you're **partitioning in-place**. One pointer tracks "last unique written", other scans forward.
The signal: *sorted array + in-place + remove something* = same-direction two pointers.

**Visual Walkthrough**
```text
arr = [1, 1, 2, 3, 3, 4]

slow = 0  (last unique element we've confirmed)
fast = 1  (scanner looking for new unique values)

─────────────────────────────────────
Initial state:

[1, 1, 2, 3, 3, 4]
 S  F

─────────────────────────────────────
Step 1: arr[fast]=1, arr[slow]=1 → SAME, skip
        (it's a duplicate, ignore it)

[1, 1, 2, 3, 3, 4]
 S     F

─────────────────────────────────────
Step 2: arr[fast]=2, arr[slow]=1 → DIFFERENT!
        slow moves up, write 2 there

[1, 1, 2, 3, 3, 4]
 S        F
 → slow += 1, arr[slow] = arr[fast]

[1, 2, 2, 3, 3, 4]
    S     F

─────────────────────────────────────
Step 3: arr[fast]=3, arr[slow]=2 → DIFFERENT!

[1, 2, 2, 3, 3, 4]
    S        F
 → slow += 1, write 3

[1, 2, 3, 3, 3, 4]
       S        F

─────────────────────────────────────
Step 4: arr[fast]=3, arr[slow]=3 → SAME, skip

[1, 2, 3, 3, 3, 4]
       S           F

─────────────────────────────────────
Step 5: arr[fast]=4, arr[slow]=3 → DIFFERENT!

→ slow += 1, write 4

[1, 2, 3, 4, 3, 4]
          S

─────────────────────────────────────
Return slow + 1 = 4  ✅
First 4 elements: [1, 2, 3, 4]
```

**The Code**
```python
def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0  # last confirmed unique position

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:  # found a new unique
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # length of unique section
```
**Time:** O(n) | **Space:** O(1)

---

### Problem C: 3Sum (Find All Triplets That Sum to Zero)
**The Problem Statement**
```text
Input:  [-4, -1, -1, 0, 1, 2]
Output: [[-1, -1, 2], [-1, 0, 1]]

Find all UNIQUE triplets that add up to 0.
```

**Why is this Two Pointers?**
3Sum = "fix one number, then run Two Pointers on the rest."
The signal: *find a combination of numbers summing to a target* — if it's pairs, it's two pointers. If it's triplets, fix one and reduce it to the pairs problem.

Think of it like this:
```text
a + b + c = 0
↓
fix a, then find: b + c = -a
                  ↑ this is just Two Sum on a sorted array!
```

**Visual Walkthrough**
```text
Sort first: [-4, -1, -1, 0, 1, 2]

─────────────────────────────────────
Outer loop fixes "a" at each index:

ITERATION 1: a = arr[0] = -4
             Need b + c = 4

[-4, -1, -1, 0,  1,  2]
  a   L               R

  L=-1, R=2 → sum = -1+2 = 1 → too small → L moves right
  L=-1, R=2 → sum = -1+2 = 1 → too small → L moves right
  L=0,  R=2 → sum = 0+2  = 2 → too small → L moves right
  L=1,  R=2 → sum = 1+2  = 3 → too small → L moves right
  L meets R → no pair found for a=-4

─────────────────────────────────────
ITERATION 2: a = arr[1] = -1
             Need b + c = 1

[-4, -1, -1, 0,  1,  2]
      a   L           R

  L=-1, R=2 → sum = -1+2 = 1 ✅ FOUND [-1, -1, 2]
              → record it, move both pointers inward

[-4, -1, -1, 0,  1,  2]
      a       L      R
              ↑  skip duplicate -1s

  L=0, R=1 → sum = 0+1 = 1 ✅ FOUND [-1, 0, 1]
             → record it, move both inward

  L meets R → done with this "a"

─────────────────────────────────────
ITERATION 3: a = arr[2] = -1
             → SAME as previous a, SKIP (avoid duplicates)

ITERATION 4: a = arr[3] = 0
             Need b + c = 0

[-4, -1, -1, 0,  1,  2]
              a   L   R

  L=1, R=2 → sum = 3 → too big → R moves left
  L meets R → done

─────────────────────────────────────
Result: [[-1,-1,2], [-1,0,1]]  ✅
```

**The Code**
```python
def three_sum(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        # skip duplicate values for the fixed element
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left, right = i + 1, len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                # skip duplicates after finding a match
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```
**Time:** O(n²) | **Space:** O(1) ignoring output

---

### Problem D: Container With Most Water
**The Problem Statement**
```text
Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49

You have vertical lines at each index.
Height of line i = arr[i]

Water between two lines = 
    width × min(left height, right height)

Find the pair that holds the MOST water.
```

**Visualizing the Setup**
```text
8   |           |
7   |           |           |
6   |   |       |           |
5   |   |   |   |           |
4   |   |   | | |           |
3   |   |   | | |   |       |
2   |   |   | | | | |       |
1 | |   |   | | | | |   |   |
  0 1   2   3 4 5 6 7   8   ← index

Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]
```
Water between index 1 (height 8) and index 8 (height 7):
```text
width  = 8 - 1 = 7
height = min(8, 7) = 7
water  = 7 × 7 = 49 ✅
```

**Why is this Two Pointers?**
The signal: *"maximize/minimize something between two ends"* on an array.

The key insight: Start with the **widest possible container** (L=0, R=end), then move inward. But which pointer do you move?

> Always move the pointer with the **shorter line.**

**Why?** Because water is limited by the shorter line. If you move the taller line inward, the width decreases AND the height can only stay the same or get worse. Moving the shorter line is your only hope of finding more water.

**Visual Walkthrough**
```text
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
       0  1  2  3  4  5  6  7  8

─────────────────────────────────────
Step 1: L=0(h=1), R=8(h=7)
        water = min(1,7) × (8-0) = 1×8 = 8
        best = 8
        → height[L] < height[R], move L right
        (the left line is the bottleneck)

[1, 8, 6, 2, 5, 4, 8, 3, 7]
 L                          R
 water=8, best=8

─────────────────────────────────────
Step 2: L=1(h=8), R=8(h=7)
        water = min(8,7) × (8-1) = 7×7 = 49
        best = 49
        → height[R] < height[L], move R left

[1, 8, 6, 2, 5, 4, 8, 3, 7]
    L                    R
    water=49, best=49

─────────────────────────────────────
Step 3: L=1(h=8), R=7(h=3)
        water = min(8,3) × (7-1) = 3×6 = 18
        best stays 49
        → move R left

[1, 8, 6, 2, 5, 4, 8, 3, 7]
    L                 R
    water=18, best=49

─────────────────────────────────────
Step 4: L=1(h=8), R=6(h=8)
        water = min(8,8) × (6-1) = 8×5 = 40
        best stays 49
        → equal height, move either (move R)

[1, 8, 6, 2, 5, 4, 8, 3, 7]
    L              R
    water=40, best=49

─────────────────────────────────────
... continuing until L meets R ...

Final answer: 49  ✅
```

**The Code**
```python
def max_water(heights):
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        h = min(heights[left], heights[right])
        w = right - left
        best = max(best, h * w)

        # move the shorter line — it's the bottleneck
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return best
```
**Time:** O(n) | **Space:** O(1)

---

### Slow & Fast Pointers — Properly Explained
This is **Flavor 2** of Two Pointers. Both pointers move in the **same direction**, but at **different speeds.**

**When do you use this?**
The signal: *linked list problems*, cycle detection, finding midpoints, or **"k steps apart"** type problems.
```text
Slow moves 1 step at a time
Fast moves 2 steps at a time
```

**The Classic Use Case: Detect a Cycle in a Linked List**
```text
Imagine a running track:

  →  →  →  →  ↓
  ↑           ↓
  ←  ←  ←  ←  ←

If two runners start at the same point,
and one runs twice as fast,
they will ALWAYS meet again if the track is circular.

If the track has an end (no cycle),
the fast runner hits the wall first.
```

**Visual: Cycle Detection**
```text
Linked list with a cycle:

1 → 2 → 3 → 4 → 5
            ↑       ↓
            7  ←  6

─────────────────────────────────────
Start: slow=1, fast=1

Step 1: slow → 2,  fast → 3
Step 2: slow → 3,  fast → 5
Step 3: slow → 4,  fast → 7  (fast goes 5→6→7)
Step 4: slow → 5,  fast → 5  ← THEY MET → CYCLE EXISTS ✅

─────────────────────────────────────
If NO cycle:

1 → 2 → 3 → 4 → None

fast hits None before they ever meet → NO CYCLE ✅
```

**The Code**
```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

        if slow == fast:
            return True  # they met = cycle exists

    return False  # fast hit the end = no cycle
```

**Slow/Fast for Finding the Middle of a Linked List**
```text
When fast reaches the END,
slow is exactly at the MIDDLE.

Why? Fast travels 2x. When fast = n steps,
     slow = n/2 steps = midpoint.

List: 1 → 2 → 3 → 4 → 5

Start: slow=1, fast=1

Step 1: slow=2, fast=3
Step 2: slow=3, fast=5 (fast.next = None, stop)

slow = 3 = middle ✅

─────────────────────────────────────

Even list: 1 → 2 → 3 → 4

Step 1: slow=2, fast=3
Step 2: slow=3, fast hits None, stop

slow = 3 = second middle (used in merge sort on linked list)
```

**Summary: Which Flavor Do I Use?**
```text
┌─────────────────────────────────────────────────────┐
│                TWO POINTERS                         │
├─────────────────────────────────────────────────────┤
│ OPPOSITE ENDS          │ SAME DIRECTION             │
│ L ──────────── R       │ slow ──── fast ────►       │
│                         │                            │
│ Use when:               │ Use when:                  │
│ • Sorted array          │ • Linked list              │
│ • Sum/pair problems     │ • Cycle detection          │
│ • Palindrome check      │ • Find middle              │
│ • Container water       │ • Remove Nth from end      │
│ • Squeeze inward        │ • "K steps apart"          │
└─────────────────────────────────────────────────────┘
```

---

## 🤔 Common Confusions & Clarifications

> **❓ Common Doubt:** *"What exactly does 'K steps apart' mean? How does that help with removing the Nth node from the end of a linked list? Also, is the 'Stock Buy and Sell' problem considered a Two Pointer problem?"*

### Let's Answer All Three

#### 1. "K Steps Apart" — What Does It Mean?
Imagine you have two runners on a track. Before they start running together, you make one runner walk ahead by exactly `K` steps first.

```text
K = 2

[1, 2, 3, 4, 5, 6, 7]
 S  .  F                ← Fast is 2 steps ahead of Slow
```

Now they both move at the same speed (1 step at a time). The gap between them never changes — it stays `K` forever.
Why is this useful? Because when `Fast` hits the end, `Slow` is automatically `K` steps behind the end. You've found a position relative to the end — without knowing the length of the list.

#### 2. Remove Nth Node From End of Linked List
**The Problem Statement**
```text
Input:  1 → 2 → 3 → 4 → 5,  N = 2
Output: 1 → 2 → 3 → 5

Remove the 2nd node from the END.
That's node with value 4.
```

**The Naive Way (Why It's Annoying)**
- Step 1: Walk the whole list → length = 5
- Step 2: Node to remove = position (5 - 2) = 3rd from start
- Step 3: Walk again to position 3, delete it
*Problem: You walked the list TWICE. What if you could do it in ONE pass?*

**The K-Steps-Apart Insight**
"If I don't know the length, but I know Fast is always N steps ahead of Slow — when Fast falls off the end, Slow must be at the node I want to delete."

**Visual Walkthrough**
```text
List: 1 → 2 → 3 → 4 → 5 → None
N = 2

─────────────────────────────────────
PHASE 1: Move Fast N steps ahead first

Start: both at head

dummy → 1 → 2 → 3 → 4 → 5 → None
        S
        F

Step 1 (move fast): 
dummy → 1 → 2 → 3 → 4 → 5 → None
        S   F

Step 2 (move fast):
dummy → 1 → 2 → 3 → 4 → 5 → None
        S       F

Fast is now N=2 steps ahead. ✅
─────────────────────────────────────
PHASE 2: Move BOTH one step at a time
         until Fast hits None

dummy → 1 → 2 → 3 → 4 → 5 → None
        S       F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
            S       F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
                S       F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
                    S       F(None)

Fast hit None. STOP. ✅
─────────────────────────────────────
WHERE IS SLOW?

Slow is at node 4.
But we need to DELETE node 4.
To delete a node, we need the node BEFORE it.

That's why we use a DUMMY node at the start
and start Slow at dummy, not head.

Let's redo with dummy:
─────────────────────────────────────
REDO with dummy node:

dummy → 1 → 2 → 3 → 4 → 5 → None
  S
  F

Phase 1: move Fast N=2 steps

dummy → 1 → 2 → 3 → 4 → 5 → None
  S         F

Phase 2: move both until Fast hits None

dummy → 1 → 2 → 3 → 4 → 5 → None
  S         F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
        S       F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
            S       F

Move both →
dummy → 1 → 2 → 3 → 4 → 5 → None
                S       F(None)

STOP. Slow is at node 3. ✅
Node 3's next is node 4 (the one to delete!)

─────────────────────────────────────
Delete: slow.next = slow.next.next

dummy → 1 → 2 → 3 → 5 → None
                ↑
                skipped over 4 ✅
```

**The Code**
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    
    slow = dummy
    fast = dummy

    # Phase 1: move fast N steps ahead
    for _ in range(n):
        fast = fast.next

    # Phase 2: move both until fast hits end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # slow is now just BEFORE the node to delete
    slow.next = slow.next.next

    return dummy.next
```

**Why the Dummy Node?**
```text
WITHOUT dummy, when N = total length,
you'd need to delete the HEAD itself.
Slow would be at head with no node before it.
You'd crash. 💥

dummy → 1 → 2 → 3 → None, N=3
  S     F          ← Fast is at head after 3 steps

Move both until fast.next = None:
  slow never moves, stays at dummy
  dummy.next = dummy.next.next
  → deletes head safely ✅

Dummy is a safety net for edge cases.
```

#### 3. Is Stock Buy and Sell a Two Pointer Problem?
**Short answer:** It looks like one, but it's actually its own pattern — sometimes called **"Kadane's-style greedy"** or just a **single-pass greedy scan.**

**The Problem**
```text
Input:  [7, 1, 5, 3, 6, 4]
Output: 5

Buy on one day, sell on a later day.
Maximize profit. You can only hold one stock.
```

**Why It LOOKS Like Two Pointers**
```text
[7, 1, 5, 3, 6, 4]
 B           S        ← Buy at 1, Sell at 6 = profit 5
```
You're picking two indices — a buy index and a sell index. Feels like two pointers, right?

**Why It's NOT Two Pointers**
In classic two pointers, you move both pointers based on a condition — squeezing inward or maintaining a gap.

But here:
- You don't squeeze inward
- You don't maintain a fixed gap
- The "sell" pointer isn't reacting to the "buy" pointer symmetrically
- **You only care about the minimum price seen so far** and whether today's price beats your best profit

The real question at each step is:
*"If I sell TODAY, what's my profit?" = today's price - lowest price I've seen so far*

**Visual Walkthrough**
```text
prices = [7, 1, 5, 3, 6, 4]

min_price = ∞
best_profit = 0

─────────────────────────────────────
Day 0: price=7
       min_price = 7
       profit if sell today = 7-7 = 0
       best = 0

[7,  1,  5,  3,  6,  4]
 ↑
 min=7, best=0

─────────────────────────────────────
Day 1: price=1
       1 < min_price → new min! min=1
       profit if sell today = 1-1 = 0
       best = 0

[7,  1,  5,  3,  6,  4]
     ↑
     min=1, best=0

─────────────────────────────────────
Day 2: price=5
       5 > min → not a new low
       profit if sell today = 5-1 = 4
       best = 4

[7,  1,  5,  3,  6,  4]
         ↑
         min=1, best=4

─────────────────────────────────────
Day 3: price=3
       3 > min → not a new low
       profit if sell today = 3-1 = 2
       best stays 4

[7,  1,  5,  3,  6,  4]
             ↑
             min=1, best=4

─────────────────────────────────────
Day 4: price=6
       6 > min → not a new low
       profit if sell today = 6-1 = 5
       best = 5  ✅

[7,  1,  5,  3,  6,  4]
                 ↑
                 min=1, best=5

─────────────────────────────────────
Day 5: price=4
       4 > min → not a new low
       profit if sell today = 4-1 = 3
       best stays 5

Answer: 5 ✅
```

**The Code**
```python
def max_profit(prices):
    min_price = float('inf')
    best_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price          # found cheaper buy day
        else:
            profit = price - min_price
            best_profit = max(best_profit, profit)

    return best_profit
```

**Pattern Comparison Table**
```text
┌──────────────────┬────────────────────────────────────┐
│ Two Pointers     │ Stock Buy & Sell                   │
├──────────────────┼────────────────────────────────────┤
│ Two active       │ One active pointer (today)         │
│ indices moving   │ One stored VALUE (min so far)      │
│ based on each    │ not a moving pointer               │
│ other            │                                    │
├──────────────────┼────────────────────────────────────┤
│ Both pointers    │ Only scan moves forward            │
│ move based on a  │ min_price just gets updated        │
│ condition        │ when a new low is found            │
├──────────────────┼────────────────────────────────────┤
│ e.g. two sum,    │ e.g. stock profit, max             │
│ container water  │ subarray sum (Kadane's)            │
└──────────────────┴────────────────────────────────────┘
```

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

> **💡 Practice Strategy:** Here is your complete, organized practice list for Pattern #1: Two Pointers — grouped by sub-pattern, ordered easy → hard within each group. *Don't look at solutions before spending at least 20 minutes on a problem!*

### Group 1: Opposite Ends — Sum Problems
*Start here. Core pattern, cleanest signal.*

| # | Problem | Difficulty |
|---|---------|------------|
| 1 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Easy |
| 2 | [3Sum](https://leetcode.com/problems/3sum/) | Medium |
| 3 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium |
| 4 | [4Sum](https://leetcode.com/problems/4sum/) | Medium |

### Group 2: Opposite Ends — String / Palindrome
*Builds on the same "squeeze inward" logic but on strings.*

| # | Problem | Difficulty |
|---|---------|------------|
| 5 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy |
| 6 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy |
| 7 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy |
| 8 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Easy |

### Group 3: Same Direction — Partition / In-Place
*Slow writer, fast scanner. The "move zeros" family.*

| # | Problem | Difficulty |
|---|---------|------------|
| 9 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy |
| 10 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy |
| 11 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy |
| 12 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium |
| 13 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium |

### Group 4: Opposite Ends — Maximize/Minimize
*Container water family. Greedy pointer movement.*

| # | Problem | Difficulty |
|---|---------|------------|
| 14 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium |
| 15 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard |

### Group 5: Slow & Fast Pointers — Linked List
*Cycle detection, middle finding, K-gap trick.*

| # | Problem | Difficulty |
|---|---------|------------|
| 16 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy |
| 17 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy |
| 18 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium |
| 19 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium |
| 20 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium |

### Group 6: Greedy Scan — Stock / Running Min-Max
*Not classic two pointers — but the "scan + track" cousin.*

| # | Problem | Difficulty |
|---|---------|------------|
| 21 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy |

### Suggested Practice Timeline
- **Week 1 — Build the foundation**
  → Problems 1, 5, 7, 9, 10, 11 (all Easy)
- **Week 2 — Apply the pattern**
  → Problems 2, 3, 6, 12, 13, 14 (Medium)
- **Week 3 — Linked list flavor**
  → Problems 16, 17, 18, 19 (Easy → Medium)
- **Week 4 — Push yourself**
  → Problems 4, 15, 20 (Medium → Hard)

---

*Notes and problems will be added here over time.*