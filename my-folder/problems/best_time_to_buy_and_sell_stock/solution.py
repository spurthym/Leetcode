class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        low=prices[0]
        max_profit=0

        for i in range(len(prices)):

            if prices[i]<low:
                low=prices[i]
            else:
                profit=prices[i]-low
                max_profit=max(max_profit,profit)
        return max_profit

