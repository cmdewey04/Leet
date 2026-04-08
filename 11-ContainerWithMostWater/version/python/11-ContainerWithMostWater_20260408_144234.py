# Last updated: 4/8/2026, 2:42:34 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l,r = 0, len(height)-1
4        vol=0
5        while l<r:
6            vol = max(vol, min(height[l], height[r]) * (r-l))
7            if height[l] < height[r]:
8                l+=1
9            else:
10                r-=1
11        return vol
12
13        
14
15
16        