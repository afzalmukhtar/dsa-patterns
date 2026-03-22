# 127. Word Ladder

**Difficulty:** Hard

**Topics:** Hash Table, String, BFS (Breadth-First Search)

---

### Problem Statement

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

### Examples

**Example 1:**
- **Input:** `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
- **Output:** `5`
- **Explanation:** One shortest transformation sequence is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`, which is 5 words long.

**Example 2:**
- **Input:** `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]`
- **Output:** `0`
- **Explanation:** The `endWord` "cog" is not in `wordList`, therefore there is no valid transformation sequence.

### Constraints
- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are unique.

---

### BFS Approach

The problem asks for the *shortest* transformation sequence, which is a classic signal for Breadth-First Search (BFS). 

1.  **Graph Representation:** Each word is a node. An edge exists between two nodes if the words differ by exactly one character.
2.  **Preprocessing:** Convert `wordList` into a `set` for $O(1)$ lookups.
3.  **Algorithm:**
    *   Start BFS from `beginWord`.
    *   For each word, generate all possible one-letter variations by changing each character from 'a' to 'z'.
    *   If a variation is in `wordList` and hasn't been visited, add it to the queue.
    *   Keep track of the "level" or number of steps. The first time we reach `endWord`, return the current step count.

```python
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if endWord not in wordList:
        return 0

    queue = deque([beginWord])
    visited = set([beginWord])
    changes = 1

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            node_list = list(node)
            for i in range(len(node_list)):
                original_char = node_list[i]
                for j in range(26):
                    char = chr(ord('a') + j)
                    if char == original_char:
                        continue
                    node_list[i] = char
                    str_new_node = "".join(node_list)
                    if str_new_node in wordList:
                        if str_new_node == endWord:
                            return changes + 1
                        if str_new_node not in visited:
                            queue.append(str_new_node)
                            visited.add(str_new_node)
                node_list[i] = original_char
        changes += 1
    return 0
```

- **Time Complexity:** $O(M^2 \times N)$, where $M$ is the length of the words and $N$ is the number of words in `wordList`.
- **Space Complexity:** $O(M \times N)$ to store the `word_set` and the BFS queue.
