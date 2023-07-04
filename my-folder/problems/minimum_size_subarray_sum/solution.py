class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=math.inf
       
        start=0
        s=0

        for end in range(len(nums)):
            rc=nums[end]
            s+=rc
            while s>=target:
                min_len=min(min_len,end-start+1)
                s=s-nums[start]
                start+=1
        
        if min_len>len(nums):
            return 0
        return min_len

