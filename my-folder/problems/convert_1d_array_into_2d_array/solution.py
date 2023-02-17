class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        if m*n !=len(original):
            return []
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(original[j])
            res.append(t)
            original=original[n:]
        return res
        