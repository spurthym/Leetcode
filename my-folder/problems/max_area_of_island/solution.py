class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        lrow=len(grid)
        lcol=len(grid[0])
        visited=set()
   
        maxarea=0
        def dfs(row,col):
            nonlocal maxarea
            nonlocal area
            visited.add((row,col))
            area+=1
            if area>maxarea:
                maxarea=area
            for dr,dc in directions:
                r=row+dr 
                c=col+dc
                if r in range(lrow) and c in range(lcol) and grid[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)
        for i in range(lrow):
            for j in range(lcol):
                if grid[i][j]==1 and (i,j) not in visited:
                    area=0
                    dfs(i,j)
        return maxarea