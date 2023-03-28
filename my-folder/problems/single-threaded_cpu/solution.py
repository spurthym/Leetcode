class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        time=0
        at=[]
        res=[]
        i=0

        while(at or i<len(tasks)):
            while i<len(tasks) and tasks[i][0]<=time:
                heappush(at,[tasks[i][1],tasks[i][2]])
                i+=1
            if not at:
                time=tasks[i][0]
            else:
                proctime,index=heappop(at)
                time+=proctime
                res.append(index)
        return res
           

