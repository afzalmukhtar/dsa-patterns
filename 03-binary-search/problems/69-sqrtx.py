def mySqrt(x):
    """
    Binary Search on the answer space (0 to x).
    Condition: mid * mid <= x
    Time: O(log x)
    Space: O(1)
    """
    if x < 2:
        return x
        
    L, R = 1, x
    ans = 0
    
    while L <= R:
        mid = L + (R - L) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid # Potential answer, but try larger
            L = mid + 1
        else:
            R = mid - 1
            
    return ans
