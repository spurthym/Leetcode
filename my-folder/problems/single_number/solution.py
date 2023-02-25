class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0

        for n in nums:
            res=n^res
        return res






        '''
        nums.sort()
        print(nums)
        i=0
        j=1
        if len(nums)==1 or nums[i]!=nums[j]:
            return nums[i]
        while j<len(nums)-2:
            if nums[i]!=nums[j]:
              
                return nums[i]
            else:
                i=i+2
                j=j+2
        if nums[j]==nums[j+1]:
            return nums[i]
        else:
            return nums[-1]
        '''