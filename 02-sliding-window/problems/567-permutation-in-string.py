from collections import Counter

class Solution:
    def checkInclusion_sorting(self, s1: str, s2: str) -> bool:
        """
        Approach 1: Sliding Window + Sorting
        
        Insight: A substring is a permutation of s1 if they have the same sorted form.
        
        Complexity:
        - Time: O((L2 - L1) * L1 log L1) where L1 = len(s1), L2 = len(s2). 
        - Space: O(L1) for the sorted substring.
        """
        if len(s1) > len(s2):
            return False
            
        s1_sorted = sorted(s1)
        n = len(s1)

        for i in range(n, len(s2) + 1):
            if s1_sorted == sorted(s2[i - n : i]):
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Approach 2: Sliding Window + Frequency Map (Optimal)
        
        Insight: Two strings are permutations if their character frequencies are identical.
        Instead of re-sorting, we just update the counts of incoming and outgoing characters.

        Complexity:
        - Time: O(L2) since we visit each character once and map comparison is O(26).
        - Space: O(1) as the character map is capped at 26 lowercase English letters.
        """
        ls1, ls2 = len(s1), len(s2)
        if ls1 > ls2:
            return False

        need = Counter(s1)
        window = Counter(s2[:ls1])

        if need == window:
            return True

        for i in range(ls1, ls2):
            # Add incoming char, remove outgoing char
            window[s2[i]] += 1
            window[s2[i - ls1]] -= 1

            if window[s2[i - ls1]] == 0:
                del window[s2[i - ls1]]

            # Compare frequencies (O(26) operation)
            if window == need:
                return True
                
        return False
