# Pattern #5: Prefix Sum

> **Status:** 🔄 In Progress | **Solved:** 1

---

## 1. What is it?
A **Prefix Sum** is a precomputed array where each index $i$ stores the sum of all elements from the start of the array up to $i$. It allows us to calculate the sum of **any** subarray in $O(1)$ time.

## 2. When do I use it?
Look for these signals:
- **Range Queries:** "Find the sum of elements from index L to R multiple times."
- **Subarray Sum Equals K:** "Count how many subarrays sum to a target value."
- **Trigger:** "I need to perform many range sum calculations, and the array doesn't change."

## 3. The Mental Model
Imagine you're walking along a path, and you're keeping track of the total distance you've covered from the start at every milestone.
```text
Array: [3, 1, 4, 2]
Prefix Sum: [3, 4, 8, 10]
             ↑  ↑  ↑   ↑
             3 3+1 3+1+4 3+1+4+2
```
To find the distance between Milestone 1 and Milestone 3, you don't re-measure. You just subtract: `Total at 3 - Total before 1`.

## 4. Brute Force First
For every range query $(L, R)$, loop from $L$ to $R$ and sum the elements.
```python
def range_sum(arr, L, R):
    total = 0
    for i in range(L, R + 1): # O(n) per query
        total += arr[i]
    return total
```
- **Time:** $O(n)$ per query, $O(n \times m)$ for $m$ queries.
- **Why it's slow:** If you ask for the same or overlapping ranges multiple times, you're doing the same additions over and over.

## 5. The Optimization Insight
The sum of subarray `arr[L...R]` is simply `prefix[R] - prefix[L-1]`.
By spending $O(n)$ time once to build the prefix array, we can answer **any** future query in $O(1)$.

## 6. The Optimal Solution
Precompute the prefix sum array.
- **Time:** $O(n)$ for precomputation, $O(1)$ per query.
- **Space:** $O(n)$ for the prefix array.

```python
def solve(arr, queries):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        
    for L, R in queries:
        total = prefix[R] - (prefix[L-1] if L > 0 else 0)
        # return or print total
```

## 7. The Template (Subarray Sum Count)
Prefix sums are often paired with a Hashmap to find subarrays that sum to $K$.
```python
def subarray_sum_count(nums, k):
    count = 0
    curr_sum = 0
    sums = {0: 1} # {prefix_sum: frequency}
    
    for x in nums:
        curr_sum += x
        # If (curr_sum - k) exists, it means a subarray ending here sums to k
        count += sums.get(curr_sum - k, 0)
        sums[curr_sum] = sums.get(curr_sum, 0) + 1
        
    return count
```

## 8. Variations and Edge Cases
- **2D Prefix Sum:** Precompute sums for rectangles in a grid to answer 2D range queries in $O(1)$.
- **Product Except Self:** Use prefix and suffix products to avoid division.
- **XOR Queries:** Prefix XOR works exactly like prefix sum because $A \oplus B \oplus A = B$.
- **0-indexing:** Using a `prefix` array of size `n+1` (where `prefix[0]=0`) often simplifies the logic (`prefix[R+1] - prefix[L]`).

## 9. Practice Problems

| # | Problem | Difficulty | Sub-Pattern |
|---|---------|------------|-------------|
| 1 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | Core Pattern |
| 2 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + Hashmap |
| 3 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix/Suffix Prod |
| 4 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | 2D Prefix Sum |
| 5 | [Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | Running Sum |
