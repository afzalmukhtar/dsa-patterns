# 02 — Sliding Window

> **Status:** 🔄 In Progress | **Problems Solved:** 3

---

## 📌 Pattern Notes

### 1. What Is It?
Imagine you're looking through a physical window at a long wall of numbers. The window has a fixed or flexible size, and you slide it from left to right — never jumping back.

At every position, you ask: "What's interesting about the numbers currently inside my window?"

The key insight: instead of recomputing from scratch each time, you just add the new element coming in and remove the old element going out.

### 2. When Do I Use It? — The Signals 🚨
Look for these trigger phrases in a problem:

| Signal | Example |
|---|---|
| "subarray" / "substring" | "Find the longest substring where..." |
| "contiguous" elements | "Contiguous subarray with sum ≥ k" |
| "maximum/minimum" of a range | "Max sum of subarray of size k" |
| "at most k distinct" | "At most 2 distinct characters" |
| "longest/shortest" that satisfies X | "Shortest subarray with sum ≥ target" |

The dead giveaway: You're searching within a sequence, and you need something about a range of consecutive elements.

### 3. The Mental Model
Think of a train moving through stations:

Stations: `[A] [B] [C] [D] [E] [F] [G]`

Window (size 3):
```text
Step 1: [A  B  C] D  E  F  G    → look inside
Step 2:  A [B  C  D] E  F  G    → drop A, gain D
Step 3:  A  B [C  D  E] F  G    → drop B, gain E
Step 4:  A  B  C [D  E  F] G    → drop C, gain F
Step 5:  A  B  C  D [E  F  G]   → drop D, gain G
```
You never restart — you just evict the leftmost passenger and board the next one on the right. That's O(n) instead of O(n²).

### 4. Two Flavors of Sliding Window
Before diving into examples, understand there are two types:

```text
FIXED SIZE window          VARIABLE SIZE window
━━━━━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━━━━━━━
Window size = k            Window grows/shrinks
 [  k elements  ]          [L ........ R]
  ↓ slides right            L and R move independently
"max sum of k elements"    "shortest subarray with sum ≥ k"
```

### 5. Brute Force First — Why It's Slow
**Problem:** Find the maximum sum of any subarray of size k.
`arr = [2, 1, 5, 1, 3, 2],  k = 3`

Brute force — try every window of size k:
```python
def max_sum_brute(arr, k):
    n = len(arr)
    max_sum = 0
    for i in range(n - k + 1):          # O(n) windows
        window_sum = 0
        for j in range(i, i + k):       # O(k) per window
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum
```
**Time: O(n × k)** — for n=10,000 and k=1,000 that's 10 million operations. 😬
**Why is this slow?** You're recomputing overlapping work:
```text
Window 1: [2  1  5]  1  3  2   → sum = 8
Window 2:  2 [1  5  1] 3  2   → sum = 7
Notice: you recomputed 1+5 TWICE! That's the wasted work.
```

### 6. The Optimization Insight — The "Aha" Moment 💡
When you slide the window one step right:
- You **lose** the leftmost element
- You **gain** the rightmost element

So instead of recomputing the whole sum:
`new_sum = old_sum - element_leaving + element_entering`

Visually:
```text
arr = [2, 1, 5, 1, 3, 2],  k = 3

         OUT              IN
          ↓                ↓
[2  1  5] 1  3  2     sum = 8
 2 [1  5  1] 3  2     sum = 8 - 2 + 1 = 7
 2  1 [5  1  3] 2     sum = 7 - 1 + 3 = 9  ← new max!
 2  1  5 [1  3  2]    sum = 9 - 5 + 2 = 6
```
One subtraction, one addition — O(1) per slide instead of O(k). Total: O(n) 🎉

### 7. The Optimal Solution

#### Fixed Window — Max Sum of Size K
```python
def max_sum_sliding(arr, k):
    # Build the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide: add right element, remove left element
    for i in range(k, len(arr)):
        window_sum += arr[i]        # gain new right
        window_sum -= arr[i - k]    # lose old left
        max_sum = max(max_sum, window_sum)

    return max_sum
```
**Time: O(n) | Space: O(1)**

#### Variable Window — Longest Substring Without Repeating Characters
This is where it gets more interesting. The window **expands** as long as the condition holds, and **shrinks** when it breaks.

**Problem:** Find the length of the longest substring with no repeating characters.
`s = "abcabcbb" → Answer: 3 ("abc")`

The strategy:
- `R` (right pointer) always moves forward — it's greedy, try to extend
- `L` (left pointer) moves forward only when the condition is violated

```python
def length_of_longest_substring(s):
    char_set = set()
    L = 0
    max_len = 0

    for R in range(len(s)):
        # Shrink window while we have a duplicate
        while s[R] in char_set:
            char_set.remove(s[L])
            L += 1
        
        char_set.add(s[R])
        max_len = max(max_len, R - L + 1)

    return max_len
```
**Time: O(n) | Space: O(k) where k = size of character set**

### 8. The Template / Skeleton

**Fixed Window Template:**
```python
def fixed_window(arr, k):
    # 1. Build first window
    window_result = initial_computation(arr[:k])
    best = window_result
    
    # 2. Slide
    for i in range(k, len(arr)):
        window_result += arr[i]      # add incoming
        window_result -= arr[i - k]  # remove outgoing
        best = update(best, window_result)
    
    return best
```

**Variable Window Template:**
```python
def variable_window(arr):
    L = 0
    window_state = {}   # or set, or counter, depending on problem
    best = 0
    
    for R in range(len(arr)):
        # 1. Expand: add arr[R] to window
        add_to_window(window_state, arr[R])
        
        # 2. Shrink: while condition violated, move L forward
        while window_is_invalid(window_state):
            remove_from_window(window_state, arr[L])
            L += 1
        
        # 3. Update answer (window is now valid)
        best = max(best, R - L + 1)
    
    return best
```

**The muscle memory you need:**
- `R - L + 1` = current window size
- Right pointer always moves forward (outer for loop)
- Left pointer moves forward only when needed (inner while loop)

### 9. Variations and Edge Cases
- **Negative numbers:** Fixed window works perfectly. But for finding "Shortest subarray with sum ≥ target" with negatives, variable sliding window BREAKS! You need Deque + Prefix Sum instead.
- **Duplicates exist:** "At most k distinct characters" → use a frequency HashMap.
- **"Exactly k" instead of "at most k":** Trick: `exactly(k) = atMost(k) - atMost(k-1)`
- **Data comes as a stream:** Fixed works perfectly. Variable works, but you can't "look ahead".
- **Multiple valid answers:** Track all windows that match, not just the best. Or if you want a count, use a HashMap of prefix sums (Pattern 5).

### 10. What Breaks If You Use the Wrong Pattern?
- **Two Pointers:** Works for sorted arrays, but fails when order matters for subarrays. You might miss valid windows.
- **Brute Force:** Works but O(n²) or O(n²k). Too slow.
- **Prefix Sum:** Can answer sum queries but doesn't "slide". Needs extra space, misses the O(1) update insight.

---

## 🕵️ Deep Dive: Variable Sliding Window Mechanics

> **❓ Common Doubt:** *"I barely understood the variable window variation. Fixed length makes sense, but variable window is weird and confusing. I want to understand how to solve it."*

### The One Sentence That Explains Everything
**R expands to find a valid window. L shrinks to optimize it.**
That's it. Everything else is just details.

### The Real-World Analogy
Imagine you're on a budget road trip 🚗
- You start with both hands on the steering wheel at mile 0
- Your right hand (R) keeps pushing forward — picking up passengers at each stop
- The moment your car gets too crowded (condition violated), your left hand (L) kicks people out from the back
- You're always asking: "What's the longest stretch I can travel while keeping the car valid?"

```text
Start:
  L
  R
  |
  🚗 ————————————————————————————→  road

R moves forward:
  L     R
  |     |
  🚗===🚗 ——————————————————→  expanding (valid)

Car gets overcrowded, L evicts from back:
      L  R
      |  |
      🚗=🚗 ——————————————→  shrink from left (restore valid)
```
R never goes back. L only moves to fix problems.

### Build the Intuition — One Step at a Time
**Problem:** Find the longest subarray where the sum ≤ 10
`arr = [3, 1, 2, 7, 4, 2, 1]`

**Phase 1: R walks forward, building the window**
```text
R points at 3 → sum = 3 ≤ 10 ✅ valid
R points at 1 → sum = 4 ≤ 10 ✅ valid
R points at 2 → sum = 6 ≤ 10 ✅ valid
R points at 7 → sum = 13 > 10 ❌ INVALID!
arr = [3, 1, 2, 7, 4, 2, 1]
       L           R
sum = 13
```

**Phase 2: L starts evicting to fix the violation**
Window is invalid. Evict from the LEFT until valid again.
```text
Evict 3 → sum = 13 - 3 = 10 ≤ 10 ✅ valid again!
arr = [3, 1, 2, 7, 4, 2, 1]
          L        R
sum = 10  (Window size = 3)
```

**Phase 3: R keeps walking**
```text
R points at 4 → sum = 14 > 10 ❌ INVALID again!
Evict 1 → sum = 13 > 10 ❌
Evict 2 → sum = 11 > 10 ❌
Evict 7 → sum = 4 ≤ 10 ✅ valid!
arr = [3, 1, 2, 7, 4, 2, 1]
                   L  R
sum = 4  (Window size = 2)

... continuing ...
```

### The 3 Questions You Ask for Every Variable Window Problem
Before writing a single line of code, answer these:
1. **WHAT makes a window VALID?** → "sum ≤ 10", "no duplicates", "at most k distinct chars"
2. **WHAT do I track inside the window?** → a sum? a set? a hashmap counting frequencies?
3. **WHAT am I optimizing?** → longest? shortest? count?
   - If LONGEST: record answer **after** fixing (window as big as possible)
   - If SHORTEST: record answer **right when it becomes valid**

### Shortest vs Longest — The One Tricky Difference
**Longest valid window** → expand until broken, shrink to fix. Record answer OUTSIDE the while loop.
```python
while invalid:
    evict L
max_len = max(max_len, R - L + 1)
```

**Shortest valid window** → expand until valid, THEN shrink as much as possible. Record answer INSIDE the while loop.
```python
while VALID:
    min_len = min(min_len, R - L + 1)
    evict L
```

---

## 🤔 Common Confusions: Sets vs HashMaps & "Have/Need" System

> **❓ Common Doubt:** *"For longest substring with at most 2 distinct characters, can I just use a Set? If it fails when characters are duplicated, do we use a hashmap counter?"*

### Why the Set Fails — One Example
`s = "e  c  e  b  a", k = 2`
```text
R=0: add 'e' → set={'e'}         ✅ 1 distinct
R=1: add 'c' → set={'e','c'}     ✅ 2 distinct
R=2: add 'e' → set={'e','c'}     ✅ still 2 distinct (e already there)

R=3: add 'b' → set={'e','c','b'} ❌ 3 distinct! Shrink.
     Evict s[L=0] = 'e' → set.remove('e') → set={'c','b'}
     L moves to 1
```
Look at the actual window now: `s = "e  c  e  b  a"` with L=1, R=3.
Window = `"c e b"`. 'e' is still in the window at index 2! But you deleted it from the set. Now your set thinks `{'c', 'b'}` (2 distinct), but the real window has 3 distinct chars.

### The HashMap Fix — Count the Copies
Instead of "is this char in the window", ask "how many of this char are in the window?"
```text
When R adds a char:    count[char] += 1
When L evicts a char:  count[char] -= 1
                       if count[char] == 0: del count[char]  ← NOW truly gone
```
**General Rule:**
- Tracking PRESENCE? → use a Set
- Tracking FREQUENCY/COUNT? → use a HashMap

> **❓ Common Doubt:** *"How does this map out for Minimum Window Substring, especially with duplicates in the target string like AABCA?"*

### The Clever Fix — The `have` vs `need` System
Instead of re-checking all characters every step, track one integer:
- `need` = number of **unique** chars in t that must be satisfied
- `have` = number of unique chars currently satisfied

Window is valid when: `have == need`.
A character `c` counts as "satisfied" when `count_window[c] >= count_t[c]`.

### Trace on Duplicates: s = "AABCAA", t = "AABCA"
`count_t = {A:3, B:1, C:1}`, `need=3`, `have=0`

```text
R=0: add A → count_win={A:1} → A: 1 >= 3? ❌ have stays 0
R=1: add A → count_win={A:2} → A: 2 >= 3? ❌ have stays 0
R=2: add B → count_win={A:2, B:1} → B: 1 >= 1? ✅ have = 1
R=3: add C → count_win={A:2, B:1, C:1} → C: 1 >= 1? ✅ have = 2
R=4: add A → count_win={A:3, B:1, C:1} → A: 3 >= 3? ✅ have = 3 == need ✅ VALID!
```

**The Critical Insight for Duplicates:**
- `have` only increments when you EXACTLY hit the threshold (`count_win[A]` goes 2 → 3).
- `have` only decrements when you DROP BELOW the threshold (`count_win[A]` goes 3 → 2).

### The Flow in Plain English
```text
OUTER LOOP (R moves forward always):
  add s[R] to window
  if s[R] in t AND just hit the exact count needed:
      have += 1

  INNER LOOP (shrink while all conditions met):
      record answer          ← window is valid, save it
      evict s[L]
      if s[L] in t AND just fell below count needed:
          have -= 1          ← condition broken, inner loop exits
      L += 1
```

---

## 🗂️ LeetCode Practice List (Grouped & Ordered)

> **💡 Practice Strategy:** Here is your clean practice list. Start with Fixed windows to get the mechanics down, then move to Variable. *Don't look at solutions before spending at least 20 minutes on a problem!*

### 🔒 Fixed Window
*The window size `k` is given to you directly.*

| # | Problem | Difficulty | What You Track |
|---|---------|------------|----------------|
| 1 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | running sum |
| 2 | [Substrings of Size Three with Distinct Chars](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | Easy | set of chars |
| 3 | [Maximum Number of Vowels in Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | vowel count |
| 4 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Medium | running sum + count |
| 5 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | frequency map |
| 6 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | frequency map |
| 7 | [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | Medium | sum + set |
| 8 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | set within window |

### 🔓 Variable Window
*The window grows and shrinks based on a condition.*

| # | Problem | Difficulty | What You Track | Longest or Shortest |
|---|---------|------------|----------------|---------------------|
| 1 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | hashmap counts | Longest |
| 2 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | running sum | Shortest |
| 3 | [Longest Subarray of 1s After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | Medium | count of zeros | Longest |
| 4 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | count of zeros flipped | Longest |
| 5 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | hashmap (≤2 distinct) | Longest |
| 6 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | freq map + max freq | Longest |
| 7 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Medium | running product | Count |
| 8 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | two freq maps + have/need | Shortest |

### Suggested Order to Attempt
**Fixed first (simpler mechanics):**
643 → 1876 → 1456 → 567 → 438

**Then variable (build up):**
LC 3 → LC 209 → LC 1004 → LC 904 → LC 424 → LC 76

---

*Notes and problems will be added here over time.*