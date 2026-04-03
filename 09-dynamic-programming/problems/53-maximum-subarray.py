from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Solves the Maximum Subarray problem using Kadane's Algorithm.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initial state: the best subarray ending at the first element
        # is just the first element itself.
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # At each step, we decide whether to add the current number to 
            # our existing subarray sum, or start a new subarray from this number.
            # (If the existing sum is negative, it's always better to start fresh!)
            curr_sum = max(nums[i], curr_sum + nums[i])
            
            # Keep track of the highest sum we've ever seen
            max_sum = max(max_sum, curr_sum)
            
        return max_sum

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    assert sol.maxSubArray(nums1) == expected1, f"Test 1 Failed: {sol.maxSubArray(nums1)}"
    
    # Test 2
    nums2 = [1]
    expected2 = 1
    assert sol.maxSubArray(nums2) == expected2, f"Test 2 Failed: {sol.maxSubArray(nums2)}"
    
    # Test 3
    nums3 = [5, 4, -1, 7, 8]
    expected3 = 23
    assert sol.maxSubArray(nums3) == expected3, f"Test 3 Failed: {sol.maxSubArray(nums3)}"

    # Test 4 (all negatives)
    nums4 = [-5, -1, -3]
    expected4 = -1
    assert sol.maxSubArray(nums4) == expected4, f"Test 4 Failed: {sol.maxSubArray(nums4)}"

    print("All tests passed!")
