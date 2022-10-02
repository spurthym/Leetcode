class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dict={}
        for i,v in enumerate(heights):
            dict[i]=v
        heights.sort()
        c=0
        for i in range(len(heights)):
            if heights[i] == dict[i]:
                continue
            c+=1
        return c
        
        
        