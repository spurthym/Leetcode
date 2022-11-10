class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for i in range(len(nums)):
            if nums[i] in d:
               
                return [i,d[nums[i]]]
           
            d[target-nums[i]]=i
            
            '''

        lookup={}
        
        for i in range(len(nums)):
            curr_val=nums[i]
            if curr_val in lookup:
                return [i,lookup[curr_val]]
                
            else:
                lookup[target-curr_val]=i

            '''