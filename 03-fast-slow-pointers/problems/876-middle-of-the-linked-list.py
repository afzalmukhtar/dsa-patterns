from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two Pointers (Fast & Slow)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        When the fast pointer (moves 2 steps) reaches the end, 
        the slow pointer (moves 1 step) will be exactly at the middle.
        """
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
