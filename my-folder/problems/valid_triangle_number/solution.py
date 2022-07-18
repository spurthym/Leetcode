class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """https://leetcode.com/problems/valid-triangle-number/discuss/1647154/Python-Easy-Solution-or-Two-pointer-Approach"""
        count=0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            left=0
            
            right=i-1
            while left<right:
                if nums[i]<nums[left]+nums[right]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return count
