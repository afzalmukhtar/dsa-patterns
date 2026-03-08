from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two Pointers (Fixed Gap) with Dummy Node
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        A dummy node is used to simplify edge cases like removing the head.
        We maintain a gap of 'n' nodes between fast and slow.
        """
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # 1. Advance fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # 2. Move both until fast reaches the last node
        # This leaves slow exactly ONE node before the target
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # 3. Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next
