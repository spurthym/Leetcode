import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s=set(nums)
        maxl=0

        for i in range(len(nums)):
            if nums[i]-1 not in s:
                l=0
                while nums[i]+l in s:
                    l+=1
                maxl=max(l,maxl)
        return maxl
