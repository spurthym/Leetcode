class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        c=0
        max_count=0
        start=0
        z_c=0
        for end in range(len(nums)):

            rc=nums[end]
            if rc==0:
                z_c+=1
                if z_c>1:
                    while nums[start]!=0:
                        if nums[start]==1:
                            c-=1
                        start+=1
                    if nums[start]==0:
                        z_c-=1
                        start+=1
                continue
    
            c+=1
            if c>max_count:
                max_count=c
        if z_c==0:
            return len(nums)-1
        return max_count