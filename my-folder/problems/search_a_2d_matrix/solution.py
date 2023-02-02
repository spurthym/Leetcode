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




        # for i in range(top,bottom):
        #     if target<=mat[i][right-1]:
        #         if mat[i][right-1] ==target:
        #             return True
        #         else:
                    
        #             top=i
        #             print("top",top)
        #             print("breaking")
        #             break
        #     elif i<bottom:
        #         continue
        #     else:
        #         return False
        # print(top)

        # while left<right:
        #     mid=left+(right-left)//2
        #     print("mid",mid)
        #     if target==mat[top][mid]:
        #         return True
        #     elif(target<mat[top][mid]):
        #         right=mid-1
        #     else:
        #         left=mid+1

        
