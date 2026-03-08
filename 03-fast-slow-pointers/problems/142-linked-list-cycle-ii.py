from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Floyd's Cycle-Finding Algorithm (Phase I & II)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Phase I: Detect if a cycle exists.
        Phase II: Find the entrance to the cycle by moving one pointer 
                 to the head and both at the same speed.
        """
        slow = fast = head

        # Phase I: Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                # Phase II: Finding the entrance
                # Reset slow to head, leave fast at meeting point
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
