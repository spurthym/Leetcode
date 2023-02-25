class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #rows=t,b
        #columns=l,r
        l,r=0,len(mat)-1
        while l<r:
            
            for i in range(r-l):
                t,b=l,r
                topl=mat[t][l+i]

                mat[t][l+i]=mat[b-i][l]
                mat[b-i][l]=mat[b][r-i]
                mat[b][r-i]=mat[t+i][r]
                mat[t+i][r]=topl
            l+=1
            r-=1

