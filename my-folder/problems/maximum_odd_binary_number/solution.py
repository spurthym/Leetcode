class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        count=0
        l=len(s)
        
        for i in range(l):
            if s[i]=="1":
                count+=1
        res=""
                
        for i in range(count-1):
            res=res+"1"
            
        for i in range(l-count):
            res=res+"0"
        res=res+"1"
        return res
            

        
