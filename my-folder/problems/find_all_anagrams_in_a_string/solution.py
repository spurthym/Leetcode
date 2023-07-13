class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        d=Counter(p)
        matched=0

        start=0
        for end in range(len(s)):
            rc=s[end]

            if rc in d:
                d[rc]-=1
                if d[rc]==0:
                    matched+=1
            if matched==len(d):
                res.append(start)
            

            if end>=len(p)-1:
                lc=s[start]
                
                if lc in d:
                    if d[lc]==0:
                        matched-=1
                    d[lc]+=1
                start+=1
        return res