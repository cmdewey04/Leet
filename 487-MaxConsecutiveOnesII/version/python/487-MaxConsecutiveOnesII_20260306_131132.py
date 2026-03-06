# Last updated: 3/6/2026, 1:11:32 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        numZero = 0
4        longest = 0
5        l = 0
6        for r in range(len(nums)):
7            #Valid
8            if nums[r]==0:
9                numZero+=1
10            #Invalid
11            while numZero > 1:
12                if nums[l]==0:
13                    numZero-=1
14                l+=1
15            #Valid
16            longest = max(longest, r-l+1)
17        return longest
18    