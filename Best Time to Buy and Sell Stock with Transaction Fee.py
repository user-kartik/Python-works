class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0

        cash = 0 
        hold = -prices[0]  
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])

        return cash