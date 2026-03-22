from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Frequency Map Approach
        Time Complexity: O(n)
        Space Complexity: O(1) (fixed character set of 26 letters)
        """
        return Counter(s) == Counter(t)

    def isAnagram_sorting(self, s: str, t: str) -> bool:
        """
        Sorting Approach
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        return sorted(s) == sorted(t)
