class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=0
            d[s[i]]+=1
         

        for each in s:
            if d[each]==1:
                return s.index(each)
        return -1


    


        
        