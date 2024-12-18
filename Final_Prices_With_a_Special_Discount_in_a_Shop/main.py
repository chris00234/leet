class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            ith = prices[i]
            jth = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= ith:
                    jth = prices[j]
                    break
            prices[i] -= jth
        return prices
