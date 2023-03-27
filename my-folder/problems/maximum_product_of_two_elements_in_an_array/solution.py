class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums=[-x for x in nums]

        heapify(nums)

        i=-1*heappop(nums)-1
        j=-1*heappop(nums)-1

        return i*j

