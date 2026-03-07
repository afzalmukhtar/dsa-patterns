class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            while not s[L].isalnum() and L < R: L += 1
            while not s[R].isalnum() and L < R: R -= 1

            if s[L].lower() != s[R].lower():
                return False
            else:
                L += 1
                R -= 1

        return True
