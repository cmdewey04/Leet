# Last updated: 2/26/2026, 1:36:55 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        nums.sort()
        for num in nums:
            if num == smallest:
                smallest+=1
        return smallest
        