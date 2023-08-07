class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i=0

        while i<len(nums):
            j=nums[i]

            if nums[i]< len(nums) and nums[i]!=nums[j]:

                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
            else:
                i+=1
        
        for i in range(len(nums)):
            if nums[i] != i :
                return i
        return len(nums)
