# Pattern #6: Hashmap / Frequency Map

> **Status:** 🔄 In Progress | **Solved:** 7

---

## 1. What is it?
A **Hashmap** (or Dictionary in Python) is a data structure that stores key-value pairs, providing average $O(1)$ time for insertions and lookups. In DSA, we often use it as a **Frequency Map** to count occurrences or a **Position Map** to store indices.

## 2. When do I use it?
Look for these signals:
- **Frequency Counting:** "Count how many times each character appears."
- **Existence Check:** "Does this number exist in the array?"
- **Mapping:** "For each number, find its corresponding index."
- **Trigger:** "I need to look something up instantly" or "I need to track counts of elements."

## 3. The Mental Model
Imagine a set of labeled drawers. When you find an item (key), you don't search every drawer. You go straight to the drawer labeled with that item and see what's inside (value).
```text
Array: [A, B, A, C]
Hashmap: {
    A: 2,
    B: 1,
    C: 1
}
```

## 4. Brute Force First
To count elements or find pairs, you might use nested loops.
```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target: return [i, j]
```
- **Time:** $O(n^2)$
- **Why it's slow:** You're scanning the array over and over to find a match. A Hashmap lets you "find" the match in $O(1)$.

## 5. The Optimization Insight
By storing what we've seen so far in a Hashmap, we turn a "search" into a "lookup." Instead of asking "Is there a 5 in the rest of the array?", we ask "Is there a 5 in our Hashmap of visited numbers?".

## 6. The Optimal Solution
Use a single pass to build and query the Hashmap.
- **Time:** $O(n)$
- **Space:** $O(n)$ (The tradeoff: extra space for faster time)

```python
def two_sum(nums, target):
    seen = {} # {value: index}
    for i, x in enumerate(nums):
        diff = target - x
        if diff in seen:
            return [seen[diff], i]
        seen[x] = i
```

## 7. The Template (Frequency Counter)
```python
def frequency_map_template(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
        
    for key, count in counts.items():
        if condition(count):
            # Record or return
            pass
```

## 8. Variations and Edge Cases
- **Group Anagrams:** Sort characters of each word and use the sorted string as the Hashmap key.
- **Top K Frequent:** Use a Hashmap to count, then a Heap (Pattern #13) or Bucket Sort to find the top $K$.
- **Longest Consecutive Sequence:** Store all numbers in a Set for $O(1)$ existence checks.
- **Space Constraints:** If the space limit is $O(1)$, you might need to use Sorting or Two Pointers instead.

## 9. Practice Problems

| # | Problem | Difficulty | Sub-Pattern |
|---|---------|------------|-------------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Lookup Map |
| 2 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Frequency Counter |
| 3 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Categorization |
| 4 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count + Select |
| 5 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Running Sum Map |
| 6 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Set Existence |
