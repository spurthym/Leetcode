class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=[False for x in range(len(nums))]
        current_permutation=[]
        res=[]
        

        def backtrack():
            if len(current_permutation)==len(nums):
                res.append(current_permutation.copy())
                return
            used_elements=[]
            for i in range(len(nums)):
                if  not used[i] and nums[i] not in used_elements:
                    used[i]=True
                    current_permutation.append(nums[i])
                    backtrack()
                    current_permutation.pop()
                    used[i]=False
                    used_elements.append(nums[i])
        backtrack()
        return res
                    



        
