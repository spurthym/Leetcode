class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows=len(grid)
        cols=len(grid[0])

        directions=[[1,0],[-1,0],[0,1],[0,-1],]

        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j,0))
        
        m=0
        while q:
            r,c,t=q.popleft()
            m=max(t,m)
            for dr,dc in directions:
                ro=dr+r
                co=dc+c

                if ro in range(rows) and co in range(cols) and grid[ro][co]==1:
                    q.append((ro,co,t+1))
                    grid[ro][co]=2
        
        for row in grid:
            if 1 in row:
                return -1
        return m