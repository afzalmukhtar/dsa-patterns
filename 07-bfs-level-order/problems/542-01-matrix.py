from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Calculates the distance to the nearest 0 for each cell in a binary matrix.
        Uses Multi-Source BFS.
        
        Time Complexity: O(M * N) - each cell visited at most once.
        Space Complexity: O(M * N) - for the queue and result matrix.
        """
        rows, cols = len(mat), len(mat[0])
        queue = deque([])
        result = [[0] * cols for _ in range(rows)]
        ones = 0

        # Initial source nodes: all cells with 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    ones += 1
        
        if ones == 0: # Handle edge case: all 0s
            return result
        
        VALID_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        dist = 0
        while queue:
            dist += 1
            level_len = len(queue)

            for _ in range(level_len):
                i, j = queue.popleft()

                for dr, dc in VALID_DIRECTIONS:
                    ni, nj = i + dr, j + dc

                    # If neighbor is valid and is a 1 that hasn't been visited
                    if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] == 1:
                        result[ni][nj] = dist
                        mat[ni][nj] = 0 # Mark as visited by flipping to 0
                        queue.append((ni, nj))
                    
        return result
