class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        vol=0
        while l<r:
            vol=(r-l)*min(height[l],height[r])
            res=max(res,vol)
            
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
            
        return res
       

    
        """
        the below code partially works
        max_vol=0
        max_height=max(height)
        max_idx=height.index(max_height)
        
        for i in range(len(height)):
            vol=height[i]*abs(max_idx-i)
            max_vol=max(max_vol,vol)
        
        return(max_vol)"""
