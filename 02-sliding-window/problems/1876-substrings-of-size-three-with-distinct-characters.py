from collections import Counter

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Count good substrings of size 3 using a sliding window and frequency map.
        
        A substring is 'good' if it has 3 distinct characters.
        Time: O(N) since we visit each character once.
        Space: O(1) since the map size is capped at 3.
        """
        if len(s) < 3:
            return 0
            
        count = Counter(s[:3])
        nums = 1 if len(count) == 3 else 0

        for R in range(3, len(s)):
            # Add incoming character
            count[s[R]] += 1
            # Remove outgoing character
            count[s[R - 3]] -= 1

            if count[s[R - 3]] == 0:
                del count[s[R - 3]]

            # Window is good if there are 3 distinct keys
            if len(count) == 3:
                nums += 1
        
        return nums
