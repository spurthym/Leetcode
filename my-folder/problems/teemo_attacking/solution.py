class Solution:
    def findPoisonedDuration(self, ts: List[int], duration: int) -> int:
        repeat=0
        for i in range(len(ts)-1):
            diff=ts[i+1]-ts[i]
            if diff<duration:
                repeat+=duration-diff
        return len(ts)*duration-repeat
            
            