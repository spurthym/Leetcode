class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res=[0 for x in range(len(nums))]
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[j]=nums[i]
                j+=1
        for k in range(j,len(nums)):
            nums[k]=0
        return nums
