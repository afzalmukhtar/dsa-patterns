from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS (Breadth-First Search) Approach
        Shortest transformation sequence is a classic BFS problem. 
        Each word is a node, and words differing by one character have an edge.
        """
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
                    
                    # Backtrack the character change for the next position
                    node_list[i] = original_char
                    
            changes += 1
            
        return 0
