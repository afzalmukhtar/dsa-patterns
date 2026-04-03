from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Computes the length of the longest consecutive elements sequence.
        Time Complexity: O(n) - each element is visited at most twice.
        Space Complexity: O(n) - for the set.
        """
        if not nums:
            return 0
            
        set_nums = set(nums)
        max_seq = 0
        
        # We iterate through the set to avoid redundant processing of duplicates
        for n in set_nums:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in set_nums:
                target = n
                # Count the length of the sequence starting from 'n'
                while target in set_nums:
                    target += 1
                
                max_seq = max(max_seq, target - n)
                
        return max_seq

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1 = [100, 4, 200, 1, 3, 2]
    expected1 = 4
    assert sol.longestConsecutive(nums1) == expected1, f"Test 1 Failed: {sol.longestConsecutive(nums1)}"
    
    # Test 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected2 = 9
    assert sol.longestConsecutive(nums2) == expected2, f"Test 2 Failed: {sol.longestConsecutive(nums2)}"
    
    # Test 3 (duplicates)
    nums3 = [1, 0, 1, 2]
    expected3 = 3
    assert sol.longestConsecutive(nums3) == expected3, f"Test 3 Failed: {sol.longestConsecutive(nums3)}"
    
    # Test 4 (empty)
    nums4 = []
    expected4 = 0
    assert sol.longestConsecutive(nums4) == expected4, f"Test 4 Failed: {sol.longestConsecutive(nums4)}"

    print("All tests passed!")
