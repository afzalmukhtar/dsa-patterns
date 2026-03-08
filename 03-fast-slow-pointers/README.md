# 03 — Fast & Slow Pointers

> **Status:** 🔄 In Progress | **Problems Solved:** 4

---

## 📌 Pattern Notes

### 1. What Is It?
Imagine two runners on a track. One is a tortoise (slow) and the other is a hare (fast). The hare runs exactly twice as fast as the tortoise.

In a linear track with an end, the hare will simply reach the finish line first. But if the track has a **cycle (a loop)**, the faster runner will eventually lap the slower runner and they will meet again.

This is **Floyd’s Cycle-Finding Algorithm** (also known as Tortoise and Hare).

### 2. When Do I Use It? — The Signals 🚨
This pattern is almost exclusively used for **Linked Lists** and **Arrays representing pointers**.

Look for these trigger phrases:
- "Detect a cycle in a linked list"
- "Find the start of a cycle"
- "Find the middle of a linked list"
- "Determine if a number is a Happy Number"
- "Find a duplicate number without extra space" (where the array can be treated as a pointer map)

### 3. The Mental Model 🧠
Think of a circular racing track:
- **Slow Pointer:** Moves 1 step at a time.
- **Fast Pointer:** Moves 2 steps at a time.

If there's no loop, the `fast` pointer hits the end (`null`).
If there **is** a loop, the `fast` pointer will eventually enter the loop, stay there, and catch up to the `slow` pointer from behind.

### 4. The "Aha" Moments 💡

#### Finding the Middle
When the `fast` runner reaches the end (distance $N$), the `slow` runner has traveled exactly half that distance ($N/2$). Thus, the `slow` pointer is at the **middle node**.

#### Detecting a Cycle
If `slow == fast` at any point (after starting), a cycle exists.

#### Finding the Start of the Cycle
This is the most non-intuitive part. If they meet at a point `M` inside the cycle:
1. Keep one pointer at the meeting point `M`.
2. Move the other pointer back to the **start** of the list.
3. Move both pointers at the **same speed** (1 step).
4. They will meet exactly at the **entrance** of the cycle.

### 5. The Optimal Solution (Template)

#### Cycle Detection
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False
```

#### Middle of Linked List
```python
def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow # Middle node
```

### 6. The 287 "Duplicate Number" Trick
Why does this work on an array?
If `nums = [1, 3, 4, 2, 2]`, we can treat it as a functional mapping:
- Index 0 → value 1
- Index 1 → value 3
- Index 3 → value 2
- Index 2 → value 4
- Index 4 → value 2 (Duplicate!)

Since two different indices (3 and 4) both point to the same value (2), this creates a "cycle" in the pointer logic. Floyd's algorithm finds the entry point of that cycle, which is the duplicate number.

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

### Group 1: Linked List Basics
| # | Problem | Difficulty | Logic |
|---|---------|------------|-------|
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Basic detection |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Find midpoint |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | Find cycle entrance |

### Group 2: Mathematical / Array Cycles
| # | Problem | Difficulty | Logic |
|---|---------|------------|-------|
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Sum of squares cycle |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | Array as pointers |

### Group 3: Advanced Applications
| # | Problem | Difficulty | Logic |
|---|---------|------------|-------|
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Midpoint + Reverse + Merge |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | Midpoint + Reverse |

---

*Notes and problems will be added here over time.*
