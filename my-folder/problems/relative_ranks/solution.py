class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[0 for _ in range(len(score))]
        ans=[0 for x in range(len(score))]
        for i in range(len(score)):
            heap[i]=score[i]*-1
        
        heapq.heapify(heap)
        
        rank=1
        for i in range(len(score)):

            if rank==1:
                ans[score.index(heappop(heap)*-1)]="Gold Medal"
            elif rank==2:
                ans[score.index(heappop(heap)*-1)]="Silver Medal"
            elif rank==3:
                ans[score.index(heappop(heap)*-1)]="Bronze Medal"
            else:
                ans[score.index(heappop(heap)*-1)]=str(rank)

            rank+=1
        return (ans)

            


