class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        mat=[[0 for _ in range(n)] for _ in range(n)]
        print((mat))
        left=0 
        right=n
        top=0
        bottom=n
        c=0
        while left<right:

            for i in range(left,right):
                c+=1
                mat[top][i]=c
            top+=1
            print(mat)

            for i in range(top,bottom):
                c=c+1
                mat[i][right-1]=c
            right-=1

            for i in range(right-1,left-1,-1):
                c=c+1
                mat[bottom-1][i]=c
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                c+=1
                mat[i][left]=c
            left+=1
        return mat

        