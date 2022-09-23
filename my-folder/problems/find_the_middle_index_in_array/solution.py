class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i,x in enumerate(nums):
            if leftsum==total-x-leftsum:
                return i
            leftsum+=x
        return -1