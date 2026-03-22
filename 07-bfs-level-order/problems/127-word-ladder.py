from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS (Breadth-First Search) Approach
        Shortest transformation sequence is a classic BFS problem. 
        Each word is a node, and words differing by one character have an edge.
        
        Time Complexity: O(M^2 * N)
          - M is the length of the words.
          - N is the total number of words in wordList.
          - We process N words, and for each, we explore M positions and try 
            26 characters, each taking O(M) to build a new string.
        Space Complexity: O(M * N)
          - To store the set of words and the BFS queue.
        """
        # Convert list to set for O(1) lookups
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1
        
        while queue:
            # Process all nodes at the current level
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return steps
                
                # Try all 1-character transformations at each position
                for i in range(len(word)):
                    original_char = word[i]
                    for j in range(26):
                        char = chr(ord('a') + j)
                        if char == original_char:
                            continue
                        
                        # Build the potential neighbor
                        neighbor = word[:i] + char + word[i+1:]
                        
                        if neighbor in word_set and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
            # Increment steps after processing one full level
            steps += 1
            
        return 0
