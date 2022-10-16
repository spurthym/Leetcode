class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        n=num//2
        
        def rev(n):
            r=0
            while n!=0:
                temp=n%10
                r=r*10+temp
                n=n//10
            return r
        
        
        for i in range(n,num):
            x=rev(i)
            if x + i == num:
                return True
        return False