class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        top=0
        bottom=len(mat)
        left=0
        right=len(mat[0])
        res=[]

        while left < right and top < bottom:

            for i in range(left,right):
                res.append(mat[top][i])
            top+=1
            for i in range(top,bottom):
                res.append(mat[i][right-1])
            right-=1

            if not (top<bottom and left<right):
                break


            for i in range(right-1,left-1,-1):
                res.append(mat[bottom-1][i])
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                res.append(mat[i][left])
            left+=1

        return res