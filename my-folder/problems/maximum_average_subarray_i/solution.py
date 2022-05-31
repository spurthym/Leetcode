import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start,max_avg,avgsum,avg=0,-math.inf,0,0
        
        
        for end in range(len(nums)):
            rc=nums[end]
            avgsum+=rc
            if end+1>=k:
                avg=avgsum/k
                if avg>max_avg:
                    max_avg=avg
                avgsum-=nums[start]
                start+=1
        return max_avg