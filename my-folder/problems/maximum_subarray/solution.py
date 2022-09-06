class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s=nums[0]
        s=0
        for end in range(len(nums)):
            if s<0:
                s=0
            rc=nums[end]
            s=s+rc

            max_s=max(max_s,s)
        return max_s
    
    