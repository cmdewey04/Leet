# Last updated: 3/6/2026, 1:58:16 PM
1class Solution:
2    def queryString(self, s: str, n: int) -> bool:
3        for i in range(1, n+1, 1):
4            check = bin(i)[2:]
5            if check not in s:
6                return False
7        return True