# Last updated: 3/5/2026, 1:56:43 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        numZero = 0
4        longest = 0
5        l = 0
6        for r in range(len(nums)):
7            if nums[r] == 0:
8                numZero+=1
9            while numZero > 1:
10                if nums[l] == 0:
11                    numZero-=1
12                l+=1
13            longest = max(longest, r-l+1)
14        return longest
15