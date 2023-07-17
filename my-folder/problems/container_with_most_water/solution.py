class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """


        start=0
        max_water_area=0
        water=1
        highest_wall=nums[0]
        end=len(nums)-1

        while start<end:
            small_wall=min(nums[start],nums[end])
            area=small_wall*(end-start)
            if area>max_water_area:
                max_water_area=area
            
            if nums[start]<nums[end]:
                start+=1
            else:
                end-=1
        return max_water_area
        

        