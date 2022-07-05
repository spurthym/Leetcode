class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r=defaultdict(set)
        c=defaultdict(set)
        
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if (matrix[row][col] in r[row] or matrix[row][col] in c[col]):
                    return False
                r[row].add(matrix[row][col])
                c[col].add(matrix[row][col])
                
        return True