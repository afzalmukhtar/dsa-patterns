class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Count max vowels in a fixed window of size k.
        
        Complexity:
        - Time: O(N) where N is length of string s.
        - Space: O(1) for the vowels set and counter.
        """
        vowels = set("aeiou")
        
        # Initial window count
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        
        max_vowels = vowel_count
        
        # Optimization: Early exit if first window is perfect
        if max_vowels == k:
            return k
        
        # Slide the window
        for i in range(k, len(s)):
            # Add incoming character
            if s[i] in vowels:
                vowel_count += 1
            
            # Remove outgoing character
            if s[i - k] in vowels:
                vowel_count -= 1
            
            # Update max
            if vowel_count > max_vowels:
                max_vowels = vowel_count
                
            # Optimization: Early exit if we hit max possible vowels
            if max_vowels == k:
                return k
        
        return max_vowels
