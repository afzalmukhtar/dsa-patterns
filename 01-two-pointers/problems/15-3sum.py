from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Three Sum problem using the Two-Pointer technique.
        
        Args:
            nums (List[int]): An array of integers.
            
        Returns:
            List[List[int]]: A list of unique triplets that sum to zero.
        """
        triplets = []
        nums.sort()  # Step 1: Sorting is crucial for Two-Pointer approach
        n = len(nums)

        for i in range(n - 2):
            # Step 2: Skip duplicates for the "fixed" first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Run Two-Pointer logic for the remaining two elements
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Step 4: Move both pointers after a successful match
                    left += 1
                    right -= 1

                    # Step 5: Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                # Step 6: Adjust pointers based on current sum
                elif total < 0:
                    left += 1  # Sum too small, need larger value
                else:
                    right -= 1  # Sum too large, need smaller value
        
        return triplets
