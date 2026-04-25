# Last updated: 4/25/2026, 2:15:08 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        #HashMap - map num to index
4        seen = {}
5        for i,num in enumerate(nums):
6            diff = target - num
7            if diff in seen:
8                return [i, seen[diff]]
9            seen[num] = i
10