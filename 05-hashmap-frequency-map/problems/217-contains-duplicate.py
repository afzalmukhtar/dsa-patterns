def containsDuplicate(nums):
    """
    Template 1: "Have I seen this before?"
    Use a HashSet to keep track of seen elements.
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
