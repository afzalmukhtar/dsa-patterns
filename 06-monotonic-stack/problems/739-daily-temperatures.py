from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for curr_day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                last_day = stack.pop()
                result[last_day] = curr_day - last_day
            
            stack.append(curr_day)
            
        return result
