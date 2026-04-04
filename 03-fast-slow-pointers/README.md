# Pattern #3: Fast & Slow Pointers (Hare & Tortoise)

> **Status:** 🔄 In Progress | **Solved:** 4

---

## 1. What is it?
Also known as **Hare & Tortoise algorithm**, this is a pointer technique where two pointers move through a sequence (usually a linked list or array) at **different speeds**.

## 2. When do I use it?
Look for these signals:
- **Linked Lists:** Finding cycles, midpoints, or the Nth node from the end.
- **Arrays:** Finding duplicates or cyclic patterns.
- **Trigger:** "Is there a cycle in this linked list?" or "Find the middle of the list in one pass."

## 3. The Mental Model
Imagine a circular running track. If two runners start at the same point, and one runs twice as fast as the other, the fast runner will eventually "lap" the slow runner. They will meet again only if the track is a loop.
```text
S = Slow (1 step)
F = Fast (2 steps)

[1 -> 2 -> 3 -> 4 -> 5 -> 3...]
 S,F
      S    F
           S         F
                S,F  <-- MET! (Cycle detected)
```

## 4. Brute Force First
To detect a cycle, you could use a Hash Set to store every node you visit. If you see a node you've already seen, there's a cycle.
```python
def has_cycle(head):
    seen = set()
    while head:
        if head in seen: return True
        seen.add(head)
        head = head.next
    return False
```
- **Time:** $O(n)$
- **Space:** $O(n)$ (The set is the problem — can we do it in $O(1)$?)

## 5. The Optimization Insight
If there is a cycle, the gap between the Fast and Slow pointers increases by 1 each step. Eventually, the gap will equal the length of the cycle, and they will land on the same node. This allows us to detect cycles without any extra memory.

## 6. The Optimal Solution
Use two pointers moving at speeds 1 and 2.
- **Time:** $O(n)$
- **Space:** $O(1)$

```python
def solve(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True # Cycle Found
    return False # No Cycle
```

## 7. The Template
```python
def fast_slow_template(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Handle Cycle Logic
            pass
    return result
```

## 8. Variations and Edge Cases
- **Middle of List:** When Fast hits the end, Slow is at the exact middle.
- **Cycle Start:** After they meet, move one back to start. Move both at speed 1. They meet at the cycle entrance.
- **Remove Nth from End:** Maintain a fixed gap of N between two pointers.
- **Arrays (Find Duplicate):** Map the array values to indices. A duplicate value creates a "cycle" in index jumping.

## 9. Practice Problems

| # | Problem | Difficulty | Sub-Pattern |
|---|---------|------------|-------------|
| 1 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Cycle Detection |
| 2 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Midpoint Finding |
| 3 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | Cycle Entrance |
| 4 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | Array Cycle |
| 5 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Logical Cycle |
