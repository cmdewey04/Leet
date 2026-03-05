# Last updated: 3/5/2026, 12:34:43 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        longest = math.inf
4        total = 0
5        l = 0
6        for r in range(len(nums)):
7            total+=nums[r]
8            while total >= target:
9                longest = min(longest, r-l+1)
10                total-=nums[l]
11                l+=1
12        return longest if longest < math.inf else 0
13
14
15        
16        