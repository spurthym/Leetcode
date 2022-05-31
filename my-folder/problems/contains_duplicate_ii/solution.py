class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        start=0
        for end in range(len(nums)):
            rc=nums[end]
            if rc not in freq:
                freq[rc]=end
            else:
                if(end-freq[rc]<=k):
                    return True
                else:
                    lc=nums[start]
                    freq[lc]=end
                    start=start+1
        
        return False
        