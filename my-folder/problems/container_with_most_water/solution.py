class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_capacity=0
        while l<=r:
            shorter_wall=min(height[l],height[r])
            area=shorter_wall*(r-l)
            max_capacity=max(area,max_capacity)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_capacity
            