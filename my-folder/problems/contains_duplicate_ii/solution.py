class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        if len(nums)<=1:
            return False
        if(len(set(nums))==len(nums)):
            return False
        for ind,val in enumerate(nums):
            if(val in freq and ind-freq[val]<=k):
                return True
            
            freq[val]=ind
        return False
                
            
        
            
        
        