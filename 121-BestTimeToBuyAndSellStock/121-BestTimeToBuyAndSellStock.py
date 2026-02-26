# Last updated: 2/26/2026, 1:36:45 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum = math.inf
        # maximum = 0
        # for num in prices:
        #     if num < minimum:
        #         minimum = num
        #     if num - minimum > maximum:
        #         maximum = num - minimum
        # return maximum

        # maxim = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         maxim = max(maxim, prices[j]-prices[i])
        # return maxim

        minim = math.inf
        maxim = 0
        for num in prices:
            if num < minim:
                minim = num
            if num-minim > maxim:
                maxim = num-minim
        return maxim

    