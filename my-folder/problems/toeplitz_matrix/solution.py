class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        rows=len(mat)
        cols=len(mat[0])
        visit=set()
        def bfs(r,c,num):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                ro,co=q.popleft()
                r=ro+1
                c=co+1
                if r>=0 and c>=0 and r<rows and c<cols and mat[r][c]==num and (r,c) not in visit:
                    visit.add((r,c))
                    q.append((r,c))

                elif r>=rows or c>=cols:
                    return True
                else:
                    return False
        b=True
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit:
                    b=bfs(i,j,mat[i][j])
                    if b ==False:
                        return False
        return True