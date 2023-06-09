class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-1*x for x in nums]
        heapq.heapify(nums)

        for i in range(k):
            elem=heappop(nums)
        return -1*elem

    