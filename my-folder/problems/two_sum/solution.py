class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx={}

        for i in range(len(nums)):
            if nums[i] in idx:
                return [i,idx[nums[i]]]
            else:
                idx[target-nums[i]]=i
            