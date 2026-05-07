# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n: int) -> int:
    """
    Binary Search on a range (1 to n).
    Time: O(log n)
    Space: O(1)
    """
    L, R = 1, n
    
    while L <= R:
        mid = L + (R - L) // 2
        res = guess(mid)
        
        if res == 0:
            return mid
        elif res == 1: # Guess is too low, target is higher
            L = mid + 1
        else: # Guess is too high, target is lower
            R = mid - 1
            
    return -1
