from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Uses the Two-Pointer technique.
        """
        L = 0
        R = len(s) - 1
        
        while L < R:
            # Swap elements in-place
            s[L], s[R] = s[R], s[L]
            
            # Move pointers towards the center
            L += 1
            R -= 1
