# Last updated: 2/26/2026, 1:36:52 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        path = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1

        def backtrack():
            if len(path) == len(nums):
                results.append(path[:])
                return
                #might need else return inside

            for key in hashmap:
                if hashmap[key] > 0:
                    path.append(key)
                    hashmap[key]-=1
                    backtrack()

                    hashmap[key]+=1
                    path.pop()

        backtrack()
        return results

            