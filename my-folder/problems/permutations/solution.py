class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        current_state=[]
        v=[0 for x in range(len(nums))]
        res=[]
        def backtrack():
            if len(current_state)==len(nums):
                res.append(current_state.copy())
                return
            
            for i in range(len(nums)):
                if v[i]==False:
                    v[i]=True
                    current_state.append(nums[i])
                    backtrack()
                    current_state.pop()
                    v[i]=False
            
        backtrack()
        return res