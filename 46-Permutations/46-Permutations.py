# Last updated: 2/26/2026, 1:36:53 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(path):
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue

                #Decision 1
                path.append(num)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return results

    



        