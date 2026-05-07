# Pattern #6: HashMap / Frequency Map 🗺️

> **Status:** 🔄 In Progress | **Solved:** 8

---

## 1. What Is It?
A HashMap is just a lookup table — instead of scanning an array to find something, you remember things as you go.

The core idea:
"I've seen this before. Let me just remember it instead of searching for it again."

A Frequency Map is a special case — you use a HashMap to count how many times something appears.

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]

freq = {
  3: 1,
  1: 2,   # ← seen twice
  4: 1,
  5: 2,   # ← seen twice
  9: 1,
  2: 1,
  6: 1
}
```

## 2. When Do I Use It? — The Signals 🚨
Look for these phrases in a problem:

| Signal in problem | What it means |
| :--- | :--- |
| **"find if X exists"** | Store things, look them up in $O(1)$ |
| **"find two numbers that sum to..."** | Store complements as you go |
| **"count frequency / occurrences"** | Frequency map |
| **"first duplicate / repeated element"** | Track what you've seen |
| **"group by / anagram / same characters"** | Use sorted key or char count as key |
| **"most frequent element"** | Frequency map + max tracking |
| **"subarray with sum = k"** | Prefix sum + HashMap |
| **"any time $O(n^2)$ search feels wasteful"** | HashMap probably helps |
| 1 | [Two Sum](./problems/1-two-sum.md) ([Sol](./problems/1-two-sum.py)) | TBD | Added from local |
| 128 | [Longest Consecutive Sequence](./problems/128-longest-consecutive-sequence.md) ([Sol](./problems/128-longest-consecutive-sequence.py)) | TBD | Added from local |
| 136 | [Single Number](./problems/136-single-number.md) ([Sol](./problems/136-single-number.py)) | TBD | Added from local |
| 217 | [Contains Duplicate](./problems/217-contains-duplicate.md) ([Sol](./problems/217-contains-duplicate.py)) | TBD | Added from local |
| 242 | [Valid Anagram](./problems/242-valid-anagram.md) ([Sol](./problems/242-valid-anagram.py)) | TBD | Added from local |
| 347 | [Top K Frequent Elements](./problems/347-top-k-frequent-elements.md) ([Sol](./problems/347-top-k-frequent-elements.py)) | TBD | Added from local |
| 49 | [Group Anagrams](./problems/49-group-anagrams.md) ([Sol](./problems/49-group-anagrams.py)) | TBD | Added from local |
| 560 | [Subarray Sum Equals K](./problems/560-subarray-sum-equals-k.md) ([Sol](./problems/560-subarray-sum-equals-k.py)) | TBD | Added from local |

**The core trigger:** You're doing a nested loop just to find or count something. HashMap collapses that inner loop to $O(1)$.

## 3. The Mental Model 🧠
Imagine you're at a party checking a guest list.

**Brute force:** Every time someone arrives, you walk through the entire list to check if they're on it. → $O(n)$ per person → $O(n^2)$ total.

**HashMap:** You scan the list once beforehand and build a lookup table. Now every check is instant. → $O(n)$ to build → $O(1)$ per lookup.

```text
Brute Force:                    HashMap:
                                
 Guest arrives                   Guest arrives
      ↓                               ↓
 Scan entire list    →→→→→→    Check the table
 [Alice, Bob, ...]               { Alice: ✓
  ↓ ↓ ↓ ↓ ↓ ↓                    Bob: ✓
  compare each one                 ... }
                                   instant!
```

## 4. Brute Force First — Two Sum Example
Problem: Given an array, find two numbers that add up to a target.

`arr = [2, 7, 11, 15],  target = 9`

Brute force — check every pair:
```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
```
**Why it's slow:** $O(n^2)$ — for every element, you scan the rest of the array. You're re-searching things you already saw.

## 5. The Optimization Insight — The "Aha" Moment 💡
Key question: When I'm at element `x`, what am I actually looking for?

`x + ? = target`
`? = target - x    ← this is the COMPLEMENT`

So instead of scanning the rest of the array for `?`... What if I remembered every number I've seen so far, so I can check for the complement instantly?

```text
arr = [2, 7, 11, 15],  target = 9

Step 1: at 2
  complement = 9 - 2 = 7
  seen = {}  → 7 not in seen
  store 2 → seen = {2: 0}

Step 2: at 7
  complement = 9 - 7 = 2
  seen = {2: 0} → 2 IS in seen! ✓
  return [seen[2], current_index] = [0, 1]
```

## 6. The Optimal Solution
```python
def two_sum(arr, target):
    seen = {}  # value → index

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i  # store AFTER checking (avoid using same element twice)

    return []
```
- **Time:** $O(n)$ — one pass
- **Space:** $O(n)$ — the HashMap stores at most $n$ elements

## 7. The Templates / Skeletons 🏗️

### Template 1: "Have I seen this before?" (HashSet)
```python
seen = set()
for x in arr:
    if x in seen:
        # found a duplicate / match
        pass
    seen.add(x)
```

### Template 2: "Find complement / pair" (HashMap)
```python
seen = {}
for i, x in enumerate(arr):
    complement = target - x
    if complement in seen:
        return [seen[complement], i]
    seen[x] = i
```

### Template 3: Frequency Map
```python
from collections import Counter
freq = Counter(arr)  # {element: count}

# OR manually:
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

### Template 4: Group by key (Anagram grouping)
```python
groups = {}
for word in words:
    key = tuple(sorted(word))  # or frozenset
    groups.setdefault(key, []).append(word)
```

### Template 5: Prefix Sum + HashMap (subarray sum = k)
```python
prefix_sum = 0
seen = {0: 1}  # sum: count (seed with 0!)
count = 0

for num in arr:
    prefix_sum += num
    # if (prefix_sum - k) exists, a subarray ending here sums to k
    count += seen.get(prefix_sum - k, 0)
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

## 8. Variations & Edge Cases
🔹 **Duplicates exist**
- If you need all pairs, don't return early — keep counting.
- If storing index and element appears twice, decide: overwrite or keep first? Two Sum stores first occurrence — that's intentional.

🔹 **Negative numbers**
- HashMaps handle negatives fine — just use them as keys.
- Watch out for prefix sum problems: `{0: 1}` seed still works.

🔹 **Anagrams (same chars, different order)**
- Key insight: two anagrams have the same sorted form.
- Use `tuple(sorted(word))` as the HashMap key.

🔹 **Can't use extra space**
- HashMap is the extra space approach.
- If $O(1)$ space is required, you often fall back to sorting + two pointers. This is a common trade-off: time vs space.

🔹 **Subarray problems (sum = k, length = k)**
- This is where prefix sum + HashMap becomes the superpower.
- The key trick: `current_prefix - k = earlier_prefix` means there's a subarray of sum $k$ between those two points.

## 🔤 Deep Dive: Anagrams — Let's Make This Click Forever
An anagram is just a word made by rearranging the letters of another word. Two words are anagrams if and only if they have exactly the same letters, in exactly the same quantities. Order doesn't matter.

**Approach 1: Sort Both Strings** ($O(n \log n)$)
```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```

**Approach 2: Frequency Map** ($O(n)$)
```python
from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

**The "Group Anagrams" Trick:** Use the Sorted Word as a Key
Since all anagrams sort to the same string, use that as the HashMap key!
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
```

---

## 🧭 Practice Roadmap

### 🟢 Stage 1: Easy — Core Concepts First
1. [Contains Duplicate (LC 217)](https://leetcode.com/problems/contains-duplicate/) — *HashSet template*
2. [Valid Anagram (LC 242)](https://leetcode.com/problems/valid-anagram/) — *Frequency map comparison*
3. [Two Sum (LC 1)](https://leetcode.com/problems/two-sum/) — *Complement lookup (core pattern)*

### 🟡 Stage 2: Medium — Build On Top
4. [Group Anagrams (LC 49)](https://leetcode.com/problems/group-anagrams/) — *Sorted word as HashMap key*
5. [Top K Frequent Elements (LC 347)](https://leetcode.com/problems/top-k-frequent-elements/) — *Frequency map + tracking max*
6. [Subarray Sum Equals K (LC 560)](https://leetcode.com/problems/subarray-sum-equals-k/) — *Prefix sum + HashMap template*

### 🔴 Stage 3: Hard — Stretch Problem
7. [Longest Consecutive Sequence (LC 128)](https://leetcode.com/problems/longest-consecutive-sequence/) — *HashSet for $O(1)$ lookup, solved in $O(n)$*

**The One-Line Intuition to Remember:**
> "When you're scanning an array and wasting time re-searching things you already visited — store them in a HashMap and look them up in $O(1)$."

---
*Built with curiosity, designed for mastery. 🚀*