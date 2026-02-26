# Last updated: 2/26/2026, 1:36:42 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
            else:
                unique.remove(num)
            

        return unique.pop()
        