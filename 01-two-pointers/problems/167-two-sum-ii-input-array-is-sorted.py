from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two Pointers approach for Two Sum II.
        
        Args:
            numbers (List[int]): A 1-indexed array of integers sorted in non-decreasing order.
            target (int): The target sum.
            
        Returns:
            List[int]: The 1-indexed indices of the two numbers.
        """
        # Initialize two pointers at both ends of the array
        left, right = 0, len(numbers) - 1
        
        while left < right:
            # Calculate the current sum
            current_sum = numbers[left] + numbers[right]
            
            # Case 1: If current sum equals target, we've found the solution
            if current_sum == target:
                return [left + 1, right + 1]
            
            # Case 2: If current sum is less than target, move left pointer to increase sum
            elif current_sum < target:
                left += 1
            
            # Case 3: If current sum is greater than target, move right pointer to decrease sum
            else:
                right -= 1
        
        # This part should never be reached according to problem constraints
        return []
