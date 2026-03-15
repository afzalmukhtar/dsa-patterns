from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Variable-Size Sliding Window
        
        This problem is equivalent to finding the longest subarray with at 
        most 2 distinct values. We use a frequency map to track the types 
        of fruits in our baskets.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - The map stores at most 3 entries before shrinking.
        """
        # Frequency map for fruits in current window
        ftypes = Counter()
        L = 0
        max_fruits = 0

        for R in range(len(fruits)):
            # Add the new fruit to our window
            ftypes[fruits[R]] += 1

            # While we have more than 2 types of fruit, shrink the window from left
            while len(ftypes) > 2:
                ftypes[fruits[L]] -= 1

                # If a fruit type is no longer in the window, remove it from the map
                if ftypes[fruits[L]] == 0:
                    del ftypes[fruits[L]]
                
                L += 1
            
            # Update the maximum number of fruits we've collected in any valid window
            max_fruits = max(max_fruits, R - L + 1)
            
        return max_fruits
