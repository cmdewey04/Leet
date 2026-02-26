# Last updated: 2/26/2026, 1:36:56 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l<r:
            m = (l+r)//2
            if nums[m] >= target:
                r = m
            else:
                l=m+1
        return l