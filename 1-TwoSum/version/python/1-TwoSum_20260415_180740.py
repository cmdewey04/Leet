# Last updated: 4/15/2026, 6:07:40 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        # bptr = 0
4        # eptr = len(nums)-1
5        # keys = []
6        # pairs = []
7        # for i,num in enumerate(nums):
8        #     pairs.append([i,num])
9        # pairs.sort(key=lambda x: x[1])
10
11        # while not keys:
12        #     if pairs[bptr][1] + pairs[eptr][1] == target:
13        #         keys.append(pairs[bptr][0])
14        #         keys.append(pairs[eptr][0])
15        #         return keys
16        #     if pairs[bptr][1] + pairs[eptr][1] > target:
17        #         eptr-=1
18        #     if pairs[bptr][1] + pairs[eptr][1] < target:
19        #         bptr+=1
20
21        #HASH MAP
22        # seen = {}
23        # for i,num in enumerate(nums):
24        #     diff = target - num
25        #     if diff in seen:
26        #         return [seen[diff], i]
27        #     seen[num] = i
28
29       seen = {}
30       for i, num in enumerate(nums):
31        diff = target - num
32        if diff in seen:
33            return [seen[diff], i]
34        seen[num] = i
35
36