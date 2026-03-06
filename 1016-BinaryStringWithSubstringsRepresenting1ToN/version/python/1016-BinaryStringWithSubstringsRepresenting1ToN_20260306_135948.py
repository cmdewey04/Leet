# Last updated: 3/6/2026, 1:59:48 PM
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            b=bin(i)[2:]
            if(b not in s):
                return False
        return True