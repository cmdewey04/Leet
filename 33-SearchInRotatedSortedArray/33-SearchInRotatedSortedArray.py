# Last updated: 2/26/2026, 1:36:57 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Key Idea to so figure out what side of array we are on
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1        
        return -1
