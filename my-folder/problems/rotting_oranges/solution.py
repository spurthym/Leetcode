from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        rows=len(grid)
        cols=len(grid[0])

        q=deque()
        
        # Add all initially rotten oranges to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        # Perform BFS to rot the oranges
        m = 0
        while q:
            ro, co, t = q.popleft()
            m = max(m, t)

            for dr, dc in directions:
                r = dr + ro
                c = dc + co

                if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == 1:
                    q.append((r, c, t+1))
                    grid[r][c] = 2

        # Check if there are any fresh oranges left
        for row in grid:
            if 1 in row:
                return -1 # if there are fresh oranges left, return -1

        return m
        
