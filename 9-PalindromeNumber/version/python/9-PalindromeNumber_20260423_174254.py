# Last updated: 4/23/2026, 5:42:54 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        num = str(x)
6        return True if num == num[::-1] else False
7        