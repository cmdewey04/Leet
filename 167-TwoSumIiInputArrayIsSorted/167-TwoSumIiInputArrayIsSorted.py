# Last updated: 2/26/2026, 1:36:39 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # bptr = 0
        # eptr = len(numbers) - 1
        # keys = []
        # while not keys:
        #     if numbers[bptr] + numbers[eptr] == target:
        #         bptr += 1
        #         eptr += 1
        #         return [bptr,eptr]
        #     if numbers[bptr] + numbers[eptr] > target:
        #         eptr-=1
        #     if numbers[bptr] + numbers[eptr] < target:
        #         bptr+=1

        seen = {}
        for i,value in enumerate(numbers):
            diff = target - value
            if diff in seen:
                return [seen[diff]+1,i+1]
            seen[value] = i
        