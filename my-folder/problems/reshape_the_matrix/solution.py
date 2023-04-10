class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
     
        if rows *cols!=r*c:
            return mat
        
        newmat=[[0 for j in range(c)] for x in range(r)]
        k=0
        for x in range(rows):
            for y in range(cols):
                newmat[k//c][k%c]=mat[x][y]
                k+=1




        return (newmat)