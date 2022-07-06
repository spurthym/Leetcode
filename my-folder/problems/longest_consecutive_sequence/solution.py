import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        if len(nums)<=1:
            return len(nums)
        start=end=0
        max_length=1
        while end+1 in range(len(nums)):
            rc=nums[end]
            if nums[end]!=nums[end+1]:
                if nums[end+1]-rc==1:
                    l=end-start+2
                    max_length=max(max_length,l)
                    end=end+1
                    continue
            start=end+1
            end=end+1
        return max_length