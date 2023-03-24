class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        n=heapq.heapify(nums)
        print(nums)
        count=0

        for i in range(len(nums)):
            temp=heappop(nums)
            if temp==0:
                heapify(nums)
                continue
            else:
                nums=[x-temp for x in nums]
                count+=1
            heapify(nums)
        print(count)


        return count