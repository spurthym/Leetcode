class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows=len(matrix)
        cols=len(matrix[0])
        zerorow=False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        zerorow=True
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0]=0
            
        if zerorow==True:
            for c in range(cols):
                matrix[0][c]=0

                
                
