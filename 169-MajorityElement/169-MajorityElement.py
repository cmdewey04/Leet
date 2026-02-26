# Last updated: 2/26/2026, 1:36:39 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return(Counter(nums).most_common(1)[0][0])
    
        