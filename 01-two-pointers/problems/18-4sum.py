from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Four Sum problem using the Two-Pointer technique.
        An extension of the 3Sum problem (O(n^3) complexity).
        
        Args:
            nums (List[int]): An array of integers.
            target (int): The sum to reach.
            
        Returns:
            List[List[int]]: A list of unique quadruplets that sum to the target.
        """
        n = len(nums)
        nums.sort()  # Sorting is crucial for Two-Pointer approach
        quads = []

        for fix_a in range(n - 3):
            # Skip duplicates for the first fixed element
            if fix_a > 0 and nums[fix_a] == nums[fix_a - 1]:
                continue

            for fix_b in range(fix_a + 1, n - 2):
                # Skip duplicates for the second fixed element
                # Ensure we only skip relative to the current outer loop starting index
                if fix_b > fix_a + 1 and nums[fix_b] == nums[fix_b - 1]:
                    continue
                
                # Standard Two-Pointer approach for the remaining two elements
                left = fix_b + 1
                right = n - 1

                while left < right:
                    total = nums[fix_a] + nums[fix_b] + nums[left] + nums[right]
                    
                    if total == target:
                        quads.append([nums[fix_a], nums[fix_b], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicates for left and right pointers
                        while left < right and nums[left] == nums[left - 1]: 
                            left += 1
                        while left < right and nums[right] == nums[right + 1]: 
                            right -= 1
                    
                    elif total < target:
                        left += 1  # Sum too small, need larger value
                    else:
                        right -= 1  # Sum too large, need smaller value
                        
        return quads
