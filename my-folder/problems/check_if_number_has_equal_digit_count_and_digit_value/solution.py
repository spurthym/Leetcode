class Solution:
    def digitCount(self, num: str) -> bool:


        d={}

        n=len(num)

        for i in range(n):
            if i not in d:
                d[i]=0
            if int(num[i]) not in d:
                d[int(num[i])]=0
     
            
            d[int(num[i])]+=1

        
        for j in range(n):
            if j in d and int(num[j])==d[j]:
                continue
            else:
                return False
        return True


