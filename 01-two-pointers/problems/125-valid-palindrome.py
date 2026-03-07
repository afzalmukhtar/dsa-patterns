class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Valid Palindrome using the Two-Pointer technique.
        
        Args:
            s (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        L = 0
        R = len(s) - 1

        while L < R:
            # Skip non-alphanumeric characters from the left
            # Using .isalnum() is crucial as it includes numbers (0-9)
            while L < R and not s[L].isalnum(): 
                L += 1
            
            # Skip non-alphanumeric characters from the right
            while L < R and not s[R].isalnum(): 
                R -= 1

            # Compare characters after converting to lowercase
            if s[L].lower() != s[R].lower():
                return False
            
            # Move pointers inward
            L += 1
            R -= 1
                
        return True
