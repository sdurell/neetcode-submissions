class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxProfit = 0
        for r in prices:
            profit = r - l
            if profit < 0:
                l = r
            maxProfit = max(maxProfit, profit)

        return maxProfit