class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk=[]
        
        for i in range(len(s)):
            n=1
            res=s[i]
            
            if stk and stk[-1][0]==s[i] and stk[-1][1]+n==k:
                for i in range(k-1): 
                    stk.pop()
            elif stk and stk[-1][0]== s[i]:
                n+=stk[-1][1]
                stk.append((res,n))
            else:
                stk.append((res,n))
        final=""    
        for i in range(len(stk)):
            final+=stk[i][0]
        return final
            
        '''stk=[]
        
        for i in range(len(s)):
            n=1
            
            if stk and stk[-1][0]==s[i] and stk[-1][1]+n==k:
                for i in range(k-1): 
                    stk.pop()
            elif stk and stk[-1][0]== s[i]:
                n+=stk[-1][1]
                stk.append((s[i],n))
            else:
                stk.append((s[i],n))
        final=""
        for i in range(len(stk)):
            final+=stk[i][0]
        return final
            
        '''
                
        