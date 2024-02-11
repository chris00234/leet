class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j = 0, 1
        min = 0
        while j != len(prices):
            if prices[j] <= prices[i]:
                i += 1
                if i >= j:
                    j += 1 
            else:
                profit = prices[j] - prices[i]
                j += 1
                if profit > min:
                    min = profit
            
        return min

        