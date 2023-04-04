class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i=0
        j=0
        s=0

        while i<len(mat) and j<len(mat):
            s+=mat[i][j]
            i+=1
            j+=1

        
        i=0 
        j=len(mat)-1
        while j>=0 and i<len(mat):
           
            if len(mat)%2!=0 and i==(len(mat)//2):
                print("mat[i][j]",mat[i][j])
                i+=1
                j-=1
                continue
            s+=mat[i][j]
            i+=1
            j-=1

        print(s)
        return s