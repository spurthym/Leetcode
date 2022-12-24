class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        v=[0 for _ in range(60)]
        count=0
        for i in range(len(time)):
            rem=time[i]%60
            if rem==0:
                count=count+v[0]
            else:
                count=count+v[60-rem]
            v[rem]+=1
        return count
    