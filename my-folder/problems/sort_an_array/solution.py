class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res=[]

        heapify(nums)
        while nums:
            res.append(heappop(nums))
        return res