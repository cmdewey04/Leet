# Last updated: 4/25/2026, 2:23:34 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        #sort the arrays
4        intervals.sort()
5        res = [intervals[0].copy()]
6        #[[1,3]]
7        for i in range(1, len(intervals)):
8            if intervals[i][0] <= res[-1][1]:
9                res[-1][1] = max(intervals[i][1],res[-1][1])
10            else:
11                res.append(intervals[i])
12        return res
13            
14
15
16
17
18
19
20
21        # intervals.sort()
22        # new = [intervals[0]]
23    
24        # for start, end in intervals[1:]:
25        #     if start <= new[-1][1]:
26        #         new[-1][1] = max(new[-1][1], end)
27        #     else:
28        #         new.append([start,end])
29        # return new
30
31        