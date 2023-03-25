class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        rows=len(mat)
        cols=len(mat[0])
        heap=[0 for x in range(rows)]

        

        for i in range((rows)):
            d={1:0}
            for j in range(cols):
                
                if mat[i][j]==1:
                    d[1]+=1
            print(d)
                    
            heap[i]=((d[1], i))
        heapify(heap)
                
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
