class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s=0
        
        for end in range(k):
            s=s+nums[end]
            res=s
        for end in range(k,len(nums)):
            s=s+nums[end]-nums[end-k]
            res=max(s,res)
            
        return res/k
            
        
        '''
        s,start,max_val,avg=0,0,0,0
        if(len(nums)==1):
            return nums[0]
            
        for end in range(len(nums)):
            rc=nums[end]
            s=s+rc
            if end-start>=k-1:
                avg=s/k
                max_val=max(max_val,avg)
                s=s-nums[start]
                start=start+1
        return max_val
        '''
            