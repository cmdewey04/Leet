# Last updated: 2/26/2026, 1:36:33 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #loop through array flip elements
        #if find another 0, inner loop to 
        #[0,1,0,3,12]
        #[1,3,12,3,12
        flag = 0

        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         for j in range(flag, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i] = nums[j]
        #                 nums[j] = 0
        #                 flag = j + 1
        #                 break 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[flag] = nums[i]
                flag+=1
        
        for i in range(flag, len(nums)):
            nums[i] = 0

        