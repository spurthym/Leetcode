class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        '''
        o(n) and o(n) space and time
        ans=[0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
            
        return ans
        '''
        #o(1) space:
        n=len(nums)
        for i in range(n):
            r=nums[i]
            b=nums[nums[i]]%n
            nums[i]=n*b+r
        
        for i in range(n):
            nums[i]=nums[i]//n

        return nums