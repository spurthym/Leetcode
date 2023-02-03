class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
    
        def feasible(speed) -> bool:
            hours=0
            for p in piles:
                hours+=math.ceil(p/speed)
                if hours>H:
                    return False
            return True

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left