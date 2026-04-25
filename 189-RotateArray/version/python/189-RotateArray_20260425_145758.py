# Last updated: 4/25/2026, 2:57:58 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        #
7        k = k % len(nums)
8        nums[:] = nums[-k:] + nums[:-k]