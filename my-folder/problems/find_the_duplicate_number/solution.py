class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0


        while i<len(nums):
            if nums[i]<i :
                return nums[i]
            while nums[i]!=i+1:
                if nums[i]==nums[nums[i]-1]:
                    return nums[i]
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp
            
            i+=1
        