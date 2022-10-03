class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        finalres=0
        yrange=len(grid[0])-2
        xrange=len(grid)-2

            
        def hourglass(grid,x,y):
            res=0

            for i in range(x,x+3):
                for j in range(y,y+3):                  
                    if (i==x+1 and j==y+0) or (i==x+1 and j==y+2):
                        continue
                    res+=grid[i][j]
            return res
        
        for i in range(xrange):
            for j in range(yrange):
                finalres=max(finalres,hourglass(grid,i,j))
        
        return finalres