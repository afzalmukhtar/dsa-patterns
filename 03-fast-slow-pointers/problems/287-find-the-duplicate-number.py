from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (Cycle Detection)
        
        This problem can be treated as finding the entry point of a cycle in a linked list.
        Each index points to nums[index]. Since there's a duplicate, multiple indices point
        to the same value, forming a cycle.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Find the intersection point of the two runners.
        # slow moves 1 step, fast moves 2 steps.
        # We start slow at nums[0] and fast at nums[nums[0]] to ensure they are inside the list
        # and move forward immediately.
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the "entrance" to the cycle (the duplicate number).
        # Keep fast at the intersection point and reset slow to the start.
        # Move both one step at a time; they will meet at the cycle entry.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
