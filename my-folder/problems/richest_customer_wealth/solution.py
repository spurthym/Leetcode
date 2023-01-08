class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r=len(accounts)
        c=len(accounts[0])
        max_s=0
        for i in range(r):
            s=0
            for j in range(c):
                s=s+accounts[i][j]
            if s>max_s:
                max_s=s
        return max_s