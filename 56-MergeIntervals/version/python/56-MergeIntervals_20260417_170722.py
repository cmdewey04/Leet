# Last updated: 4/17/2026, 5:07:22 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        new = [intervals[0]]
5    
6        for start, end in intervals[1:]:
7            if start <= new[-1][1]:
8                new[-1][1] = max(new[-1][1], end)
9            else:
10                new.append([start,end])
11        return new
12
13        