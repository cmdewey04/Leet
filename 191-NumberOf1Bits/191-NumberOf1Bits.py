# Last updated: 2/26/2026, 1:36:38 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans+=1
            n = n & (n-1)   
        return ans
        