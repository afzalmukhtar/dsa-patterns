class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Valid Palindrome II using Two-Pointer technique.
        Allows for at most one character deletion.
        """
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                # If mismatch found, try skipping either the left or the right character
                return is_pal(L + 1, R) or is_pal(L, R - 1)
            L += 1
            R -= 1
            
        return True
