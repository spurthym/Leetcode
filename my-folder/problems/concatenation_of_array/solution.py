class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''n=len(nums)
        ans=[ 0 for i in range(n*2)]
        print(ans)
        
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return (ans)'''
        
        n=nums.copy()
        nums.extend(nums)
        return nums