import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        max_sum,w_sum=-math.inf,0
       
        for i in nums:
            if w_sum<0:
                w_sum=0
            w_sum+=i
            
            
            max_sum=max(max_sum,w_sum)
            
        return(max_sum)