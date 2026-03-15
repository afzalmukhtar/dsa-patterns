class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Count max vowels in a fixed window of size k.
        
        Strategy: Use a fixed sliding window + an integer to track vowels count.
        
        Complexity:
        - Time: O(N) where N is length of string s.
        - Space: O(1) for the vowels set and counter.
        """
        vowels = set("aeiou")
        
        # Initial window count
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowel = current_vowels
        
        # Slide the window
        for i in range(k, len(s)):
            # If incoming is a vowel
            if s[i] in vowels:
                current_vowels += 1
            
            # If outgoing was a vowel
            if s[i - k] in vowels:
                current_vowels -= 1
            
            # Update max if current window has more
            if current_vowels > max_vowel:
                max_vowel = current_vowels
                
            # Early exit if we hit max possible vowels
            if max_vowel == k:
                return k
        
        return max_vowel
