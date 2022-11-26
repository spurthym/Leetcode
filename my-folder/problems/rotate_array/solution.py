class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k=k%len(nums)
        l=0
        r=len(nums)-1
        
        def helper(l,r,nums):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r-=1
        
        helper(l,r,nums)
        helper(0,k-1,nums)
        helper(k,len(nums)-1,nums)
        