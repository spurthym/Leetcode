class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        low=prices[0]
        for end in range(1,len(prices)):
            if prices[end]<low:
                low=prices[end]
            diff=abs(low-prices[end])
            max_profit=max(max_profit, diff)
        return max_profit