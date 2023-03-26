class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=0

        for i in range(len(num)):
            s=s*10+num[i]
        s=s+k
        res= list(str(s))
        res=[eval(i) for i in res]

        return res
            