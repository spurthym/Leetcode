class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}

        for i in range(len(nums)):
            if nums[i] in lookup:
                return [i,lookup[nums[i]]]
            
            
            lookup[target-nums[i]]=i
         
            

        
        
        