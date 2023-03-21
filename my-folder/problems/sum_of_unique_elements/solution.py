class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        s=0
        d={}

        for i in range(len(nums)):

            if nums[i] not in d:
                d[nums[i]]=1
                s+=nums[i]
            elif d[nums[i]]==1:
                d[nums[i]]+=1
                s-=nums[i]
            else:
                continue
        return s

