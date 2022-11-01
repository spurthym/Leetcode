class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        bmap={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        
        for each in s:
            if each in bmap:
                if l and l[-1]==bmap[each]:
                    l.pop()
                else:
                    return False
            else:
                l.append(each)
        return True if not l else False
    
        