class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        
        while True:
            slow=self.finds(slow)
            fast=self.finds(self.finds(fast))
            if slow==fast:
                break
        return slow==1
    def finds(self,n):
        s=0
        while n>0:
            d=n%10
            s+=d*d
            n=n//10
        return s
            
        