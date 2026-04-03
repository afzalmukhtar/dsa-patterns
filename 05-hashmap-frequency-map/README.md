# 05 — HashMap / Frequency Map

> **Status:** 🔄 In Progress | **Problems Solved:** 7

---

## 📌 Pattern Notes

### 1. What Is It?
A HashMap is just a lookup table — instead of scanning an array to find something, you remember things as you go.
The core idea: *"I've seen this before. Let me just remember it instead of searching for it again."*

A **Frequency Map** is a special case — you use a HashMap to count how many times something appears.
```python
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
freq = { 3: 1, 1: 2, 4: 1, 5: 2, 9: 1, 2: 1, 6: 1 }
```

### 2. When Do I Use It? — The Signals 🚨
Look for these phrases in a problem:

| Signal in problem | What it means |
|---|---|
| "find if X exists" | Store things, look them up in $O(1)$ |
| "find two numbers that sum to..." | Store complements as you go |
| "count frequency / occurrences" | Frequency map |
| "first duplicate / repeated element" | Track what you've seen |
| "group by / anagram / same characters" | Use sorted key or char count as key |
| "most frequent element" | Frequency map + max tracking |
| "subarray with sum = k" | Prefix sum + HashMap |
| "any time $O(n^2)$ search feels wasteful" | HashMap probably helps |

The core trigger: You're doing a nested loop just to find or count something. HashMap collapses that inner loop to $O(1)$.

### 3. The Mental Model 🧠
Imagine you're at a party checking a guest list.
- **Brute force:** Every time someone arrives, you walk through the entire list to check if they're on it. → $O(n)$ per person → $O(n^2)$ total.
- **HashMap:** You scan the list once beforehand and build a lookup table. Now every check is instant. → $O(n)$ to build → $O(1)$ per lookup.

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

### 4. Brute Force First — Two Sum Example
**Problem:** Given an array, find two numbers that add up to a target.
`arr = [2, 7, 11, 15],  target = 9`

Brute force — check every pair ($O(n^2)$):
```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
```
You're *re-searching* things you already saw.

### 5. The Optimization Insight — The "Aha" Moment 💡
Key question: When I'm at element `x`, what am I actually *looking for*?
`x + ? = target  →  ? = target - x` (this is the COMPLEMENT)

So instead of scanning the rest of the array for `?`...
**What if I remembered every number I've seen so far, so I can check for the complement instantly?**

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

### 6. The Optimal Solution
```python
def two_sum(arr, target):
    seen = {}  # value → index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i  # store AFTER checking
    return []
```
**Time:** $O(n)$ | **Space:** $O(n)$

### 7. The Templates / Skeletons 🏗️

**Template 1: "Have I seen this before?"**
```python
seen = set()
for x in arr:
    if x in seen: pass # found duplicate
    seen.add(x)
```

**Template 2: "Find complement / pair"**
```python
seen = {}
for i, x in enumerate(arr):
    complement = target - x
    if complement in seen: return [seen[complement], i]
    seen[x] = i
```

**Template 3: Frequency Map**
```python
from collections import Counter
freq = Counter(arr)  # {element: count}
```

**Template 4: Group by key (Anagram grouping)**
```python
groups = {}
for word in words:
    key = tuple(sorted(word))
    groups.setdefault(key, []).append(word)
```

**Template 5: Prefix Sum + HashMap (subarray sum = k)**
```python
prefix_sum, count, seen = 0, 0, {0: 1}
for num in arr:
    prefix_sum += num
    count += seen.get(prefix_sum - k, 0)
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

### 8. Variations & Edge Cases
- **Duplicates exist:** If you need all pairs, keep counting. "Two Sum" stores the first occurrence by design.
- **Can't use extra space:** If $O(1)$ space is required, fall back to sorting + two pointers. Trade-off: time vs space.
- **Most frequent element:** `Counter(arr).most_common(k)`

---

## 🕵️ Deep Dive: Understanding Anagrams and Hash Keys

> **❓ Common Doubt:** *"Can you explain anagrams? I often find them confusing and difficult, especially 'Group Anagrams'."*

### What Even IS an Anagram?
An anagram is just a word made by rearranging the letters of another word.
`"eat"` → rearrange → `"tea"`
**The Key Insight:** Two words are anagrams if and only if they have *exactly the same letters, in exactly the same quantities*.

### Two Ways to Check "Same Inventory"
**Approach 1: Sort Both Strings**
If two words have the same letters, sorting them produces the identical string.
`"eat"` → sort → `"aet"`, `"tea"` → sort → `"aet"`
*Simple, but $O(n \log n)$ because sorting takes time.*

**Approach 2: Frequency Map (HashMap way)**
Count how many times each letter appears in both words. If counts match perfectly → anagram.
```python
from collections import Counter
def is_anagram(s, t): return Counter(s) == Counter(t)
```
*Faster, $O(n)$ time.*

### The "Group Anagrams" Problem
Given `["eat", "tea", "tan", "ate", "nat", "bat"]`.
**The Trick:** Since all anagrams sort to the same string, use that sorted string as the **HashMap key**.
```text
"eat" → sorted → "aet"  ┐
"tea" → sorted → "aet"  ├── all map to "aet" bucket
"ate" → sorted → "aet"  ┘
"tan" → sorted → "ant"  ┐
"nat" → sorted → "ant"  ┴── both map to "ant" bucket
"bat" → sorted → "abt"  ── alone
```
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in groups: groups[key] = []
        groups[key].append(word)
    return list(groups.values())
```

**Common Confusions Fixed:**
- *"Are 'a' and 'aa' anagrams?"* No. Letter *counts* must match exactly.
- *"Why use sorted string as key?"* Because `"eat"` and `"tea"` are different strings (different hash keys). But `sorted("eat") == sorted("tea") == "aet"`.

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

> **💡 Practice Strategy:** Here are the core problems to practice, ordered from simplest concept (HashSet) to the hardest integration (Prefix + HashMap).

### 🟢 Easy — Core Concepts First

| # | Problem | Concept Taught |
|---|---------|----------------|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | "Have I seen this before?" — HashSet template |
| 2 | [Valid Anagram](./problems/242-valid-anagram.md) | Frequency map comparison, `Counter(s) == Counter(t)` |
| 3 | [Two Sum](./problems/1-two-sum.md) | Complement lookup — the core HashMap insight |
| 4 | [Single Number](./problems/136-single-number.md) | Frequency counting (though XOR is the optimal space solution) |

### 🟡 Medium — Build On Top

| # | Problem | Concept Taught |
|---|---------|----------------|
| 5 | [Group Anagrams](./problems/49-group-anagrams.md) | Using `sorted(word)` or a freq tuple as a HashMap key |
| 6 | [Top K Frequent Elements](./problems/347-top-k-frequent-elements.md) | Frequency map + tracking max frequency |
| 7 | [Subarray Sum Equals K](./problems/560-subarray-sum-equals-k.md) | Prefix sum + HashMap template — the `{0: 1}` seed trick |

### 🔴 Hard — Stretch Problem

| # | Problem | Concept Taught |
|---|---------|----------------|
| 8 | [Longest Consecutive Sequence](./problems/128-longest-consecutive-sequence.md) | HashSet for $O(1)$ lookup, must solve in $O(n)$ without sorting |

---

*Notes and problems will be added here over time.*