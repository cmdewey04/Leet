# Last updated: 2/26/2026, 1:36:56 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums,target,True)
        last = self.binarySearch(nums,target,False)
        return [first,last]       

    def binarySearch(self,nums, target, first):
        l,r = 0, len(nums) - 1
        index = -1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                index = m
                if first:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return index

