class Solution:

    def isPal(self, s: str, L: int, R: int):
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

            
    def validPalindrome(self, s: str) -> bool:
        L = 0 
        R = len(s) - 1

        
        while L < R:
            if s[L] != s[R]:
                return self.isPal(s, L + 1, R) or self.isPal(s, L, R - 1)
            L += 1
            R -= 1
        return True
