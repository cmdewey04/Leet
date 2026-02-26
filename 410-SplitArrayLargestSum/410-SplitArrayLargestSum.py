# Last updated: 2/26/2026, 1:36:27 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count+=1
            return count <= k


        l,r = max(nums), sum(nums)
        while l<r:
            m = (l+r)//2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l
        