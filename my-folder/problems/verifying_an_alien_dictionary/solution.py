class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i in range(26):
            d[order[i]]=i
        print(d)

        for i in range(1,len(words)):
            m=0
            n=0
            while m < len(words[i-1]) and n<len(words[i]):
                if d[words[i-1][m]] < d[words[i][n]]:
                    break
                if d[words[i-1][m]] > d[words[i][n]]:
                    return False
                m += 1
                n += 1
                if n == len(words[i]) and m < len(words[i-1]):
                    return False
        return True
            
