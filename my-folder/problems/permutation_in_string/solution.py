class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        matched=0
        start=0

        for end in range(len(s2)):
            rc=s2[end]
            if rc in s1:
                d[rc]-=1
                if d[rc]==0:
                    matched+=1
            print(matched)
            if matched==len(d):
                return True

            if end>=len(s1)-1:
                lc=s2[start]
                if lc in d:
                    if d[lc]==0:
                        matched-=1

                    d[lc]+=1
                start+=1
        return False


