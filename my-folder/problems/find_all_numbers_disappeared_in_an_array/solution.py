class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i=0
        n=len(nums)

        while i<n:
            j=nums[i]-1
            if nums[i]!=nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
            else:
                i+=1
        
        res=[]
        print(nums)

        for i in range(n):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
