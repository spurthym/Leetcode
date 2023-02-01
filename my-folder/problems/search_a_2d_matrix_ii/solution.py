class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        c=len(matrix[0])-1
        print(r,c)
        print(len(matrix))
        while(r<=len(matrix)-1 and c>=0):
            if matrix[r][c]==target:
                return True
            if(matrix[r][c]<target):
                r+=1
            else:
                c-=1
        return False