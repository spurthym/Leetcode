class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()
        i=0

        while i<len(nums) and nums[i]<0 and k>0  :
            
            nums[i]*=-1
            i+=1
            k-=1
        nums.sort()
        if k%2!=0:
            nums[0]*=-1
        print(nums)
        
        return (sum(nums))
