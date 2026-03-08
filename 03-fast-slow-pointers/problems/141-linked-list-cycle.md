# 141. Linked List Cycle

**Difficulty:** Easy

**Topics:** Linked List, Two Pointers (Fast & Slow)

---

### Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Examples

**Example 1:**
- **Input:** `head = [3,2,0,-4], pos = 1`
- **Output:** `true`
- **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**
- **Input:** `head = [1,2], pos = 0`
- **Output:** `true`

**Example 3:**
- **Input:** `head = [1], pos = -1`
- **Output:** `false`

### Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

### Fast and Slow Pointers (Floyd's Cycle-Finding)

This approach uses two pointers moving at different speeds to detect a cycle.

1. **Slow Pointer:** Moves one step at a time.
2. **Fast Pointer:** Moves two steps at a time.

If a cycle exists, the fast pointer will eventually "lap" the slow pointer and they will meet at the same node. If the fast pointer reaches the end of the list (`null`), then no cycle exists.

```python
def hasCycle(head: Optional[ListNode]) -> bool:
    # Standard Floyd's loop: handles empty/single-node cases naturally
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            return True

    return False
```

- **Time Complexity:** $O(n)$ - In the worst case, the fast pointer traverses the list twice.
- **Space Complexity:** $O(1)$ - Constant extra memory.
