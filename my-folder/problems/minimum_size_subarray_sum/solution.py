class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        min_l=len(nums)+1
        s=0
        for end in range(len(nums)):
            rc=nums[end]
            s=s+rc
            
            while(s>=target):
                min_l=min(min_l,end-start+1)

                lc=nums[start]
                s-=lc
                start=start+1
                
            
        if(min_l>len(nums)):
            return 0
        return min_l