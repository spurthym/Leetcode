class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[x*-1 for x in stones]
        heapify(stones)
        
        while(len(stones)>1):
            
            l=heappop(stones)
            s=heappop(stones)

            heappush(stones,l-s)
        return -1*stones[0]



        

                

