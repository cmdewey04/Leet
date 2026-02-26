# Last updated: 2/26/2026, 1:36:43 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num-1 not in numbers:
                count = 0
                while num+count in numbers:
                    count+=1
                longest = max(longest, count)
        return longest
