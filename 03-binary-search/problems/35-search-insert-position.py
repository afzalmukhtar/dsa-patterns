def searchInsert(nums, target):
    """
    Binary Search to find the insertion point.
    If not found, L will be at the correct insertion index.
    Time: O(log n)
    Space: O(1)
    """
    L, R = 0, len(nums) - 1
    
    while L <= R:
        mid = L + (R - L) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
            
    # When loop ends, L is the index where target should be inserted
    return L
