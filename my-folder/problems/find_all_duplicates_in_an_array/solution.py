class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res=[]
        i=0
        while(i<len(nums)):
            j=nums[i]-1
            if nums[i]!=nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])

        return res