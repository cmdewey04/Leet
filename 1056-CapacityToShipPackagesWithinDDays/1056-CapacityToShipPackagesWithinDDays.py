# Last updated: 2/26/2026, 1:36:23 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Create feasible function to determine if can ship packages with capacity C
        def feasible(c):
            d = 1
            shipment = 0
            for weight in weights:
                shipment += weight
                if shipment > c:
                    shipment = weight
                    d+=1
            return d <= days

        l,r = max(weights), sum(weights)
        while l < r:
            m = (l+r)//2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l

        