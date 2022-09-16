class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        mat1=[[None]*rows for  _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                mat1[c][r]=matrix[r][c]
        return mat1
        