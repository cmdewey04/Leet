# Last updated: 2/26/2026, 1:36:44 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = [0] * len(prices)
        # for i in range(len(prices)-2, -1, -1):
        #     diff = prices[i+1] - prices[i]
        #     if diff > 0: 
        #         profits[i] += diff
        #     profits[i] += profits[i+1]
        # return max(profits)
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]  

        return profit


        