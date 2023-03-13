class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s=0
        l=[]
        res=[]
        candidates.sort()
        print(candidates)
        def backtrack(pos,target,l):
            if target==0:
                res.append(l.copy())
                return
            elif(target<=0):
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i]==prev:
                    continue
                l.append(candidates[i])
                backtrack(i+1,target-candidates[i],l)
                l.pop()
                prev=candidates[i]
            
        backtrack(0,target,l)
        print(res)
        return res