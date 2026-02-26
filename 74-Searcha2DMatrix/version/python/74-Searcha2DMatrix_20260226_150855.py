# Last updated: 2/26/2026, 3:08:55 PM
1import math
2class Solution:
3    def minEatingSpeed(self, piles: List[int], h: int) -> int:
4        # #Binary Search over possible k values
5        # l,r = 1, max(piles)
6        # while l<=r:
7        #     k = (l+r)//2
8        #     hours = 0
9        #     for p in piles:
10        #         hours += math.ceil(p/k)
11        #     if hours <= h:
12        #         r = k -1
13        #     elif hours > h:
14        #         l = k + 1
15            
16        # return l
17        def feasible(k):
18            count = 0
19            for num in piles:
20                count += math.ceil(num/k)
21            return count <= h
22
23
24        l,r = 1, max(piles)
25        while l < r:
26            m = (l+r)//2
27            if feasible(m):
28                r = m 
29            else:
30                l = m + 1
31        return l
32