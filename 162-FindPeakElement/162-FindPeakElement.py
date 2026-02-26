# Last updated: 2/26/2026, 1:36:40 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #at middle check if either side is greater, go to greater side
        #if stuck, return index
        l,r=0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            #take right route to find peak
            if m+1 < len(nums) and nums[m+1] > nums[m]:
                l = m + 1
            #take left route to find peak
            elif m-1 >= 0 and nums[m-1] > nums[m]:
                r = m - 1
            else:
                return m
        return 0