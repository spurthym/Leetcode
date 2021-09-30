class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        u=''
        start=0
        count=0
        for end in range(len(s)):
                rc=s[end]
                u=u+rc
                
                while(len(u)>=3):
                    if(len(set(u))==3):
                        count+=1
                    start=start+1
                    u=u[1:]
                
        return count
            
                
                
            
            