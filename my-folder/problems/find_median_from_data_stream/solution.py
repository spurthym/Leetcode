class MedianFinder:

    def __init__(self):
        self.stk=[]
        self.n=0
        

    def addNum(self, num: int) -> None:
        self.stk.append(num)
        
        self.n+=1
        
        

    def findMedian(self) -> float:
        self.stk.sort()
        if self.n %2==0:
            return ((self.stk[self.n//2]+self.stk[(self.n//2)-1])/2)
        
        else:
            return self.stk[self.n//2]
        
        


    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()