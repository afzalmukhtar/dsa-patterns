from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Longest substring without repeating characters using a variable sliding window.
        
        Pattern: Variable Sliding Window
        - R expands the window.
        - L shrinks the window when a duplicate is found (count[s[R]] > 1).
        
        Complexity:
        - Time: O(N) where N is the length of the string. Each character is visited at most twice.
        - Space: O(K) where K is the size of the character set (English letters, digits, symbols).
        """
        L = 0
        max_len = 0
        count = Counter()

        for R in range(len(s)):
            # 1. Expand: add current character to frequency map
            count[s[R]] += 1

            # 2. Shrink: while current character is a duplicate, move L forward
            while count[s[R]] > 1:
                count[s[L]] -= 1
                if count[s[L]] == 0:
                    del count[s[L]]
                L += 1
            
            # 3. Update result: window is now valid (no duplicates)
            max_len = max(max_len, R - L + 1)
            
        return max_len
