class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
     
        if rows*cols!=r*c:
            return mat
        newmat= [ [0 for _ in range(c)] for _ in range(r)]

        l=[]
        k=0   
        for i in range(rows):
            for j in range(cols):
                l.append(mat[i][j])

        for i in range(r):
            for j in range(c):
                newmat[i][j]=l[k]
                k+=1
        
        return newmat