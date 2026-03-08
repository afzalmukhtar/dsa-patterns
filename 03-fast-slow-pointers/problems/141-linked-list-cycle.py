from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Standard Floyd's Cycle-Finding Algorithm
        
        This version is slightly cleaner:
        1. Starts both pointers at head (implicitly handles head/head.next is None).
        2. Uses 'is' for object identity comparison.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
                
        return False
