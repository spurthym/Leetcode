class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        left=0
        right=len(mat[0])-1
        top=0
        bottom=len(mat)-1

        while top<=bottom:
            midrow=(top+bottom)//2
            if target>mat[midrow][-1]:
                top=midrow+1
            elif target<mat[midrow][0]:
                bottom=midrow-1
            else:
                break
        if not(top<=bottom):
            return False
        
        while left<=right:
            midcol=(left+right)//2
            
            if target>mat[midrow][midcol]:
                left=midcol+1
                
            elif target<mat[midrow][midcol]:
                right=midcol-1
            else:
                return True
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

        
