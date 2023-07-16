class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i=0
        l=0
        r=len(nums)-1

        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp

        while i<=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            if nums[i]==2:
                swap(r,i)
                r-=1
                i-=1
            

            i+=1