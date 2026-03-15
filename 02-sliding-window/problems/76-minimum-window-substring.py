from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Variable-Size Sliding Window (Have vs Need Strategy)
        
        This problem asks for the minimum window containing all characters 
        from t. We track our current window with a frequency map and 
        use a 'have' variable to count how many requirements we've met.
        
        Time Complexity: O(m + n)
        Space Complexity: O(k) - At most 52 unique characters.
        """
        from collections import Counter

        t = Counter(t)
        window = Counter()
        
        need = len(t)
        have = 0
        
        min_size = float("inf")
        min_string = ""
        L = 0

        for R in range(len(s)):
            window[s[R]] += 1

            if s[R] in t and window[s[R]] == t[s[R]]:
                have += 1
            
            while need == have:
                if (R - L + 1) < min_size:
                    min_size = R - L + 1
                    min_string = s[L: R + 1]

                window[s[L]] -= 1

                if s[L] in t and window[s[L]] < t[s[L]]:
                    have -= 1

                if window[s[L]] == 0:
                    del window[s[L]]
                
                L += 1
        return min_string
