from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        Calculates the height of land cells based on their distance to water.
        Uses Multi-Source BFS.
        
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        """
        rows, cols = len(isWater), len(isWater[0])
        queue = deque([])
        # Result matrix: -1 signifies unvisited/unprocessed
        result = [[-1] * cols for _ in range(rows)]

        # Find all sources: Water cells (height = 0)
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    result[r][c] = 0
                    queue.append((r, c))

        # Standard Multi-Source BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if the cell has been visited
                if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == -1:
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr, nc))
                    
        return result
