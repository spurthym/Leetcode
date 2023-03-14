class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res=[]
        current_state=[]
        v=[False]*len(nums)

        def backtrack(current_state):
            if len(current_state)==len(nums):
                res.append(current_state.copy())
                return
            s=[]
            for i in range(len(nums)):
                if nums[i] not in s and v[i]==False:
                    current_state.append(nums[i])
                    v[i]=True
                    backtrack(current_state)
                    current_state.pop()
                    s.append(nums[i])
                    v[i]=False
        backtrack(current_state)
        return res

