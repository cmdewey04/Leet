# Last updated: 4/29/2026, 9:33:51 AM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        s[:] = s[::-1]
7    
8        