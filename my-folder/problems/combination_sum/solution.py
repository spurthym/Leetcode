class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        res = []
        s=0
        candidates.sort()
        
        def backtrack(start,s):
            if s > target:
                return
            if s == target:
                res.append(temp.copy())
                return
            for i in range(start, len(candidates)):
                
                if s + candidates[i] > target:  # added condition
                    break
                temp.append(candidates[i])
                print(temp)
                s += candidates[i]
                backtrack(i,s)
                temp.pop()
                s -= candidates[i]


                
        backtrack(0,s)
        return res
