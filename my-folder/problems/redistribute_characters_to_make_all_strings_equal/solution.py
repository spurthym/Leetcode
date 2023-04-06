class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        d={}

        for each in words:
            for c in each:

                if c not in d:
                    d[c]=0
                d[c]+=1
        print(d)
        for v in d.values():
           
            if len(words)>1 and  v%len(words)!=0:
                return False
        return True
