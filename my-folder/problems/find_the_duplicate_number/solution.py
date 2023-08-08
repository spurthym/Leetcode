class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0

        while i<len(nums):
            if nums[i]!=i+1:
                j=nums[i]-1
                if nums[i]!=nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                else:
                    return nums[i]
            else:
                i+=1
   
            
        