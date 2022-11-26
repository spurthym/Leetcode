class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
        
        
        
        '''
        total=0
        min_val=prices[0]
        profit=0
        for i in range(1,len(prices)-1):
            if(prices[i]<min_val):
                min_val=prices[i]
                continue
            if((prices[i]-min_val)>profit):
                                                              
                profit=prices[i]-min_val
                min_val=prices[i+1]
                total=total+profit
                profit=0
        return total'''