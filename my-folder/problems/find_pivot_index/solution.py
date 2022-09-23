class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        print(total)
        leftsum=0
        for i,x in enumerate(nums):
            if leftsum==total-x-leftsum:
                return i
            leftsum+=x
        return -1

        