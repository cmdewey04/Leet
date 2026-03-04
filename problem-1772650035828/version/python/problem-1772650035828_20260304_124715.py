# Last updated: 3/4/2026, 12:47:15 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        longest = float('inf')
4        total = 0
5        l=0
6        for r in range(len(nums)):
7            total += nums[r]
8            while total >= target:
9                longest = min(longest, r-l+1)
10                total-=nums[l]
11                l+=1
12                
13        return longest if longest != float('inf') else 0
14                
15
16        
17        