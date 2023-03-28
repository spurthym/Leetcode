class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        for i in range(len(arr)):
            arr[i]=[abs(arr[i]-x),arr[i]]
        heapify(arr)
        res=[]

        for i in range(k):
            diff,val=heappop(arr)
            res.append(val)
        res.sort()
        return res
        