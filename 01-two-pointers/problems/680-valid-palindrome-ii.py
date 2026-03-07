class Solution:
    def isPal(self, s: str, L: int, R: int):
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        L = 0 
        R = len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return self.isPal(s, L + 1, R) or self.isPal(s, L, R - 1)
        return True
