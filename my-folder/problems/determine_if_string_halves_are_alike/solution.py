class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i=0
        m=len(s)/2
        c=0
        while i<m:
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                c+=1
            i+=1
        while i<len(s):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                c-=1
            i+=1
            
        return c==0