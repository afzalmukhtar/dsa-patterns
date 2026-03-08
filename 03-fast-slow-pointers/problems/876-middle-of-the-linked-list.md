# 876. Middle of the Linked List

**Difficulty:** Easy

**Topics:** Linked List, Two Pointers (Fast & Slow)

---

### Problem Statement

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second middle** node.

### Examples

**Example 1:**
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[3,4,5]`
- **Explanation:** The middle node of the list is node 3.

**Example 2:**
- **Input:** `head = [1,2,3,4,5,6]`
- **Output:** `[4,5,6]`
- **Explanation:** Since the list has two middle nodes with values 3 and 4, we return the second one.

### Constraints
- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

---

### Fast and Slow Pointers (Middle Detection)

This is a classic application of the fast and slow pointers pattern.

1. **Slow Pointer:** Moves **one** step at a time.
2. **Fast Pointer:** Moves **two** steps at a time.

By the time the `fast` pointer reaches the end of the list, the `slow` pointer will have travelled exactly half the distance, landing on the middle node.

- For **odd length** (e.g., 5 nodes): `fast` lands on the last node, `slow` is at the 3rd node.
- For **even length** (e.g., 6 nodes): `fast` lands on `null`, `slow` is at the 4th node (the second middle).

```python
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

- **Time Complexity:** $O(n)$ - Single pass through the list.
- **Space Complexity:** $O(1)$ - Constant extra space.
