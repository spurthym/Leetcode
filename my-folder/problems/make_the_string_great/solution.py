class Solution:
    def makeGood(self, s: str) -> str:
        # res=""
        # for i in range(1,len(s)):
        #     if s[i]==s[i-1].lower() or s[i].lower==s[i-1] or s[i]==s[i-1].upper() or s[i].upper==s[i-1]:
        #         continue
        #     res=res+s[i-1]
        # return res
        stk=[]
        
        for i in range(len(s)):
            if stk and (ord(stk[-1])==ord(s[i])-32 or ord(stk[-1])==ord(s[i])+32):
                stk.pop()
            else:
                stk.append(s[i])
        
        return "".join(stk)
            
            
        