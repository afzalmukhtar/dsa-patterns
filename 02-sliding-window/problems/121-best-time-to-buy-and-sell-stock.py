from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimal Single-Pass Greedy Scan
        
        This approach tracks the minimum price encountered so far and 
        calculates the maximum profit by subtracting that minimum from 
        each subsequent day's price.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_profit = 0
        last_min = float("inf")
    
        for price in prices:
            # Update the minimum price we've seen so far
            if price < last_min:
                last_min = price
            # Calculate potential profit if we sold today
            elif price - last_min > max_profit:
                max_profit = price - last_min
        
        return max_profit

# Alternative version using built-in min/max functions:
# def maxProfit(self, prices: List[int]) -> int:
#     max_profit = 0
#     last_min = float("inf")
#     for price in prices:
#         last_min = min(last_min, price)
#         max_profit = max(max_profit, price - last_min)
#     return max_profit
