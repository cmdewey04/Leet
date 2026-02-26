# Last updated: 2/26/2026, 1:36:30 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1,n+1):
            index =  i
            while index != 0:
                index = index & (index-1)
                ans[i] += 1
        return ans
        

        


        

        