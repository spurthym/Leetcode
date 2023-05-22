class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]

        candidates.sort()

        def backtrack(s,start):
            if s>target:
                return

            if s==target:
                res.append(temp.copy())
                return
            
            for i in range(start,len(candidates)):
                if s+candidates[i]>target:
                    break
                
                s+=candidates[i]
                temp.append(candidates[i])
                backtrack(s,i)
                temp.pop()
                s-=candidates[i]
        

        backtrack(0,0)
        return res
