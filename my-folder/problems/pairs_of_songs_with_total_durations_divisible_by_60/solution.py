class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        time_shortage=[0 for _ in range(60)]
        count=0

        for vals in time:
            rem=vals%60
            if rem==0:
                count+=time_shortage[0]
            else:
                count+=time_shortage[60-rem]
            time_shortage[rem]+=1
        return count
    