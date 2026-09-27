class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        notes
        Want to maximize profit -> greedy
        maxProfit starts at 0
        To maximize proft, want the left side to be as low as possible and right to be as high
        sliding window problem
        '''

        s, e = 0, 0
        maxProfit = 0
        while s < len(prices) and e < len(prices):
            profit = prices[e] - prices[s]
            while profit < 0 and s < len(prices):
                s += 1
                profit = prices[e] - prices[s]
            maxProfit = max(maxProfit, profit)
            e += 1
        return maxProfit
