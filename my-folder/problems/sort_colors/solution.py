class Solution:
    def sortColors(self, n: List[int]) -> None:
        p1,p2,p3=0,0,len(n)-1
        while p2<=p3:
            if n[p2]==0:
                n[p1],n[p2]=n[p2],n[p1]
                p1+=1
                p2+=1
            elif n[p2]==1:
                p2+=1
            else:
                n[p2],n[p3]=n[p3],n[p2]
                p3-=1
            
                
                