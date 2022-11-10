class Solution:
    def isValid(self, s: str) -> bool:
        d={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stk=[]
        for i in range(len(s)):
            if stk and s[i] in d:
                if stk[-1]==d[s[i]]:
                    stk.pop()
                    continue
                else:
                    return False
            
            
            stk.append(s[i])
        return True if not stk else False