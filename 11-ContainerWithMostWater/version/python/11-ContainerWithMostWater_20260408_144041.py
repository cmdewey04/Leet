# Last updated: 4/8/2026, 2:40:41 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        def calculate_height(l,r):
4            return min(height[l], height[r]) * (r-l)
5        l,r = 0, len(height)-1
6        vol=0
7        while l<r:
8            vol = max(vol, calculate_height(l,r))
9            if height[l] < height[r]:
10                l+=1
11            else:
12                r-=1
13        return vol
14
15        
16
17
18        