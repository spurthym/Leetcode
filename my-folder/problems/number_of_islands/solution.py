class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        island=0
        directions=[[-1,0],[1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                ro,co=q.popleft()
                for dr,dc in directions:
                    r=ro+dr
                    c=co+dc
                    if (r in range(rows) and c in range(cols) and 
                       grid[r][c]=="1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
        
        
        
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island
        