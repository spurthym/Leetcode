class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        res = []
        candidates.sort()

        def backtrack(start, s):
            if s > target:
                return
            if s == target:
                res.append(temp.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:  # skip duplicates
                    continue
                if s + candidates[i] > target:
                    break
                temp.append(candidates[i])
                backtrack(i+1, s+candidates[i])
                temp.pop()

        backtrack(0, 0)
        return res
