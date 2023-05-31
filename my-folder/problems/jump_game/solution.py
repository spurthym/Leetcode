class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        gp=l-1
        for i in range(l-1,-1,-1):
            if (i-1)+nums[i-1]>=gp:
                gp=i-1
            if gp==0:
                return True
        return False
