class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(comb: List[int], start: int, k: int):
            if k == 0:
                res.append(comb[:])
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(comb, i+1, k-1)
                comb.pop()

        res = []
        backtrack([], 1, k)
        return res