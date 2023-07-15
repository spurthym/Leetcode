class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0 
        r=len(nums)-1
        res=[]

        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                res.append(nums[r]*nums[r])
                r-=1
            else:
                res.append(nums[l]*nums[l])
                l+=1
        return res[::-1]


