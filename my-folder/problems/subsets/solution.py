class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        curr_ss=[]

        def backtrack(start):
            res.append(curr_ss.copy())
            for i in range(start, n):
                curr_ss.append(nums[i])
                backtrack(i + 1)
                curr_ss.pop()
              
        backtrack(0)
        return res
