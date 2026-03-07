class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Reverse only vowels in a string using the Two-Pointer technique.
        """
        # Using a set for O(1) lookup time
        vowels = set("aeiouAEIOU")
        
        # Strings are immutable in Python, convert to list for in-place swaps
        chars = list(s)
        L, R = 0, len(s) - 1

        while L < R:
            # Move L until it finds a vowel or meets R
            while L < R and chars[L] not in vowels:
                L += 1
            
            # Move R until it finds a vowel or meets L
            while L < R and chars[R] not in vowels:
                R -= 1
            
            # Swap vowels and move pointers inward
            chars[L], chars[R] = chars[R], chars[L]
            L += 1
            R -= 1
            
        return "".join(chars)
