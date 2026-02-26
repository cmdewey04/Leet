# Last updated: 2/26/2026, 1:36:24 PM
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       #[3,6,7,11], h = 8
       #[1,2,3,4,5,6,7,8,9,10,11]
        l,r=1,max(piles)
        i = 0
        while l<=r:
            k = (l+r)//2
            time = self.hoursToEat(piles,k)
            if time <= h:
                i = k
                r = k - 1
            else:
                l = k + 1
        return i

    
    def hoursToEat(self,piles,speed):
        hours = 0
        for p in piles:
            hours += math.ceil(p/speed)
        return hours