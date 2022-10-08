class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9 + 7
        preSum = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                preSum[i][j] = preSum[i][j+1] + preSum[i+1][j] - preSum[i+1][j+1] + (pizza[i][j] == 'A')
                
        @lru_cache(None)
        
        def dp(k, r, c):
            if (preSum[r][c] == 0):
                return 0
        
            if (k == 0):
                return 1
        
            ans = 0
            
            for i in range(r, m):
                if (preSum[r][c] - preSum[i][c] > 0):
                    ans = (ans + dp(k-1, i, c))%MOD
                    
            
            for j in range(c, n):
                if (preSum[r][c] - preSum[r][j] > 0):
                    ans = (ans + dp(k-1, r, j))%MOD
                    
            return ans
        
        return dp(k-1, 0, 0)
        