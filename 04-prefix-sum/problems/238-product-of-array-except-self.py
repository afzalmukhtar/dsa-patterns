from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements of nums except nums[i] for each i.
        Time Complexity: O(n)
        Space Complexity: O(1) (excluding output array)
        """
        left = [1]
        right = 1
        n = len(nums)
        for i in range(1, n):
            left.append(left[i - 1] * nums[i - 1])

        for i in range(n - 1, -1, -1):
            left[i] *= right
            right *= nums[i]

        return left

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    assert sol.productExceptSelf(nums1) == expected1, f"Test 1 Failed: {sol.productExceptSelf(nums1)}"
    
    # Test 2
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    assert sol.productExceptSelf(nums2) == expected2, f"Test 2 Failed: {sol.productExceptSelf(nums2)}"
    
    print("All tests passed!")
