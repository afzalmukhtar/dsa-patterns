# 142. Linked List Cycle II

**Difficulty:** Medium

**Topics:** Linked List, Two Pointers (Fast & Slow)

---

### Problem Statement

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (0-indexed). It is `-1` if there is no cycle. **Note that `pos` is not passed as a parameter.**

**Do not modify the linked list.**

### Examples

**Example 1:**
- **Input:** `head = [3,2,0,-4], pos = 1`
- **Output:** `tail connects to node index 1`

**Example 2:**
- **Input:** `head = [1,2], pos = 0`
- **Output:** `tail connects to node index 0`

### Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

### Floyd's Cycle-Finding Algorithm (Two Phases)

This problem builds on cycle detection by adding a second phase to find the exact entry point.

#### Phase 1: Detection
Use the standard fast and slow pointers. If they meet, a cycle exists. If the fast pointer reaches the end, there is no cycle.

#### Phase 2: Finding the Entrance
Once a meeting point is found:
1.  Keep one pointer at the meeting point.
2.  Move the other pointer back to the `head`.
3.  Move **both** pointers one step at a time.
4.  The node where they meet is the start of the cycle.

**Mathematical Proof:**
Let $L_1$ be the distance from head to cycle entrance, and $L_2$ be the distance from entrance to meeting point.
$Slow\_distance = L_1 + L_2$
$Fast\_distance = L_1 + L_2 + n \times C$ (where $C$ is cycle length)
Since $Fast = 2 \times Slow$:
$L_1 + L_2 + n \times C = 2(L_1 + L_2) \implies L_1 = n \times C - L_2$
This means the distance from head to entrance ($L_1$) is equal to the distance from meeting point to entrance (traversing through the rest of the cycle).

```python
def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    
    return None
```

- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$
