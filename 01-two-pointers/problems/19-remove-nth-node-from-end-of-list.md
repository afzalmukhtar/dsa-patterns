# 19. Remove Nth Node From End of List

**Difficulty:** Medium

**Topics:** Linked List, Two Pointers

---

### Problem Statement

Given the `head` of a linked list, remove the $n^{th}$ node from the end of the list and return its head.

### Examples

**Example 1:**
- **Input:** `head = [1,2,3,4,5], n = 2`
- **Output:** `[1,2,3,5]`

**Example 2:**
- **Input:** `head = [1], n = 1`
- **Output:** `[]`

**Example 3:**
- **Input:** `head = [1,2], n = 1`
- **Output:** `[1]`

### Constraints
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

### Two Pointers (Fixed Gap Pattern)

To remove the $n^{th}$ node from the end in a single pass, we use two pointers maintained at a distance of $n$ from each other.

#### Why use a Dummy Node?
Using a `dummy` node that points to the head is the cleanest way to handle the edge case where the **head node itself** needs to be removed (i.e., when $n$ equals the length of the list). It allows `slow` to be positioned at a node "before" the head.

#### Algorithm:
1.  Initialize `dummy` node pointing to `head`.
2.  Set `slow` and `fast` pointers at `dummy`.
3.  Move `fast` forward $n$ times.
4.  Move both `fast` and `slow` forward until `fast.next` is `None`.
5.  `slow` is now pointing to the node **immediately before** the one we want to delete.
6.  Update `slow.next = slow.next.next`.
7.  Return `dummy.next`.

```python
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = fast = dummy
    
    # Create the n-step gap
    for _ in range(n):
        fast = fast.next
        
    # Maintain the gap until fast reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    # Delete the target node
    slow.next = slow.next.next
    
    return dummy.next
```

- **Time Complexity:** $O(n)$ - Single pass.
- **Space Complexity:** $O(1)$ - Constant extra space.
