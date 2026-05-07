def search(nums, target):
    """
    Classic Binary Search (Pattern A: L <= R)
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
            
    return -1
