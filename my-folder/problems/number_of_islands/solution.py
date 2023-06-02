class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        lrow=len(grid)
        lcol=len(grid[0])
        visited=set()
        count=0
        stack=[]
        q=collections.deque()
        def bfs(row,col):

            q.append((row,col))

            while (q):
                q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc

                    if r in range(lrow) and c in range(lcol) and grid[r][c]=="1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
                        bfs(r,c)
            







        for i in range(lrow):
            for j in range(lcol):
                if grid[i][j]=="1" and (i,j) not in visited:

                    count+=1
                    bfs(i,j)
                   
        return count




        