def countNegatives(grid):
    """
    Binary Search on each row to find the first negative number.
    Time: O(m * log n)
    Space: O(1)
    """
    count = 0
    n = len(grid[0])
    
    for row in grid:
        # Find first negative in this row
        L, R = 0, n - 1
        first_neg_idx = n
        
        while L <= R:
            mid = L + (R - L) // 2
            if row[mid] < 0:
                first_neg_idx = mid
                R = mid - 1 # Try to find an earlier negative
            else:
                L = mid + 1
        
        count += (n - first_neg_idx)
        
    return count
