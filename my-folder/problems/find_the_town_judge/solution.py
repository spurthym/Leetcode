class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in range(1,n+1):
            d[i]=[]
        print(d)
        for j in range(len(trust)):
            d[trust[j][0]].append(trust[j][1])
        print(d)
        
        
        for each in d:
            if len(d[each])==0:
                for k in d:
                    if k ==each:
                        continue
                    if each not in d[k]:
                        return -1
                return each
                    

                
        
        return -1
