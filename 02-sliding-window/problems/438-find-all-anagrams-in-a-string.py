from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find start indices of all anagrams using a fixed sliding window.
        
        Complexity:
        - Time: O(N) where N is length of string s. Map comparison is O(26).
        - Space: O(1) for the character frequency maps (size <= 26).
        """
        l1 = len(p)
        l2 = len(s)

        if l1 > l2:
            return []
        
        result = []
        need = Counter(p)
        window = Counter(s[:l1])

        if need == window:
            result.append(0)
        
        for i in range(l1, l2):
            # Incoming character
            window[s[i]] += 1
            # Outgoing character
            window[s[i - l1]] -= 1

            if window[s[i - l1]] == 0:
                del window[s[i - l1]]
            
            # Substring starting at (i - l1 + 1)
            if window == need:
                result.append(i - l1 + 1)

        return result
