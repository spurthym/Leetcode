class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l=max(weights)
        r=sum(weights)

        def feasible(capacity):
            total=0
            days =1
            for w in weights:
                total+=w
                if total>capacity:
                    days+=1
                    total=w
                    if days>D:
                        return False
            return True


        while l<r:
            mid=l+(r-l)//2
            if feasible(mid):
                r=mid
            else:
                l=mid+1
        return l