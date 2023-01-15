class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        j=0
        l=[]
        while m!=0:
            l1=[]
            for i in range(j,j+n):
                l1.append(original[i])
            l.append(l1)
            m-=1
            j=j+n
        return l
