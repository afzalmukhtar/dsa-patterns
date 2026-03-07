from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Three Sum Closest problem using the Two-Pointer technique.
        
        Args:
            nums (List[int]): An array of integers.
            target (int): The target sum.
            
        Returns:
            int: The sum of the three integers that is closest to the target.
        """
        # Step 1: Sorting is essential for the two-pointer approach
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Step 2: Fix the first element (Pin)
            left = i + 1
            right = n - 1

            while left < right:
                # Step 3: Calculate current sum and distance
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If current sum is exactly target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Step 4: Move pointers based on current sum (Squeeze)
                if current_sum < target:
                    left += 1  # Need a larger sum to get closer to target
                else:
                    right -= 1  # Need a smaller sum to get closer to target
        
        return closest_sum
