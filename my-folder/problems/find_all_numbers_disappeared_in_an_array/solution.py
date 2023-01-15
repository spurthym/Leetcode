class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        l=[]

        for i in range(len(nums)):
            n=nums[i]
            j=abs(n)-1
            nums[abs(nums[i])-1]=abs(nums[j])*-1
        
        for i,n in enumerate(nums):
            if n>0:
                l.append(i+1)
        return l