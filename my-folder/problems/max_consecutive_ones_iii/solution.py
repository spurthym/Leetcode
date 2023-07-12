class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len=0
        z_c=0
        start=0

        for end in range(len(nums)):
            rc=nums[end]
            if rc==0:
                z_c+=1
                if z_c>k:
                    # if end-start-1>max_len:
                    #     max_len=end-start-1
                    while nums[start]!=0:
                        start+=1
                    if nums[start]==0:
                        start+=1
                        z_c-=1
                    continue
                
            if end-start+1>max_len:
                max_len=end-start+1
        return max_len