from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS Approach:
        1. We first scan the grid to find all initial rotten oranges and count fresh ones.
        2. We only add the rotten ones to our queue. We don't need to add empty cells (0) 
           or fresh ones (1) initially.
        3. Using BFS, we rot adjacent fresh oranges layer by layer (minute by minute).
        4. In each step, we only add a neighbor to the queue if it is FRESH (1). 
           - If it's already rotten (2), we skip it (no need to rot again).
           - If it's empty (0), we skip it (nothing to rot).
        5. When we rot a fresh orange:
           - We add it to the queue for the next minute.
           - We decrement the 'fresh' count.
           - We mark it as rotten (2) in the grid.
        6. We use a VALID_DIRECTIONS list to simplify the 4-directional search.
        """
        rotten = deque([])
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        
        # Step 1: Initialize the queue with all sources (rotten oranges)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        # Base Case: No fresh oranges to rot
        if fresh == 0:
            return 0
        
        VALID_DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        time = -1
        
        # Step 2: Process the ripples (BFS)
        while rotten:
            time += 1
            level_len = len(rotten)

            for _ in range(level_len):
                r, c = rotten.popleft()

                for dr, dc in VALID_DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundaries and if the neighbor is fresh
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # ROT the orange
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))

        # If fresh > 0, some oranges were unreachable (separated by empty slots)
        return time if fresh == 0 else -1
