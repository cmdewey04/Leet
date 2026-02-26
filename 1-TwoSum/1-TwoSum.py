# Last updated: 2/26/2026, 1:37:02 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bptr = 0
        # eptr = len(nums)-1
        # keys = []
        # pairs = []
        # for i,num in enumerate(nums):
        #     pairs.append([i,num])
        # pairs.sort(key=lambda x: x[1])

        # while not keys:
        #     if pairs[bptr][1] + pairs[eptr][1] == target:
        #         keys.append(pairs[bptr][0])
        #         keys.append(pairs[eptr][0])
        #         return keys
        #     if pairs[bptr][1] + pairs[eptr][1] > target:
        #         eptr-=1
        #     if pairs[bptr][1] + pairs[eptr][1] < target:
        #         bptr+=1

        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i