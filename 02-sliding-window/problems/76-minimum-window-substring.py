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
        if not t or not s:
            return ""

        # Frequency map for string t
        count_t = Counter(t)
        # Number of unique characters in t that need to be satisfied
        need = len(count_t)
        # Number of unique characters currently satisfied in window
        have = 0
        
        window = Counter()
        min_size = float("inf")
        # Store indices of the best window to avoid O(m) slicing inside loop
        res = [-1, -1]
        
        L = 0
        for R in range(len(s)):
            char = s[R]
            window[char] += 1
            
            # If the current character is in t and hits the exact requirement
            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            # While window is valid, try to shrink it
            while have == need:
                # Update our result if current window is smaller
                if (R - L + 1) < min_size:
                    min_size = R - L + 1
                    res = [L, R]
                
                # Pop from the left
                left_char = s[L]
                window[left_char] -= 1
                
                # If we remove a required character and it falls below count_t
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                L += 1
                
        L, R = res
        return s[L : R + 1] if min_size != float("inf") else ""
