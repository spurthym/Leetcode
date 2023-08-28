class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        c=0
        no_of_rows=len(grid)
        no_of_cols=len(grid[0])
        visited=set()


        def bfs(i,j):
            q=deque()
            q.append([i,j])
            
            while q:
                row,col=q.popleft()
                grid[row][col]=-1
                for  dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if (r,c) not in visited  and r in range(no_of_rows) and c in range(no_of_cols) and grid[r][c]=="1":
                        q.append([r,c])
                        visited.add((r,c))

        for i in range(no_of_rows):
            for j in range(no_of_cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    c+=1
        return c
