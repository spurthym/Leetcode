class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        '''
        if len(s)!= len(t):
            return False
        lookup={}
        matched=0
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]]=0
            lookup[s[i]]+=1

        
        
        for c in range(len(t)):
            if t[c] in lookup:
                lookup[t[c]]-=1
                if lookup[t[c]]==0:
                    del lookup[t[c]]
                matched +=1
                if matched==len(t):
                    return True
            else:
                return False
        
        