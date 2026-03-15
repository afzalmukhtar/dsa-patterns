class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Approach 1: Sliding Window + Sorting
        
        Insight: A substring is a permutation of s1 if they have the same sorted form.
        
        Complexity:
        - Time: O((L2 - L1) * L1 log L1) where L1 = len(s1), L2 = len(s2). 
                The window slides (L2 - L1) times, and each slide triggers a sort.
        - Space: O(L1) for the sorted substring.
        
        Note: While intuitive, this approach might exceed time limits for very large inputs (L1, L2 ~ 10^4).
        """
        if len(s1) > len(s2):
            return False
            
        s1_sorted = sorted(s1)
        n = len(s1)

        # Slide a fixed window of size n
        for i in range(n, len(s2) + 1):
            # If the sorted substring matches the sorted s1, a permutation exists
            if s1_sorted == sorted(s2[i - n : i]):
                return True
                
        return False
