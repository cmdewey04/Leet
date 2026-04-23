# Last updated: 4/23/2026, 5:43:22 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        num = str(x)
4        return True if num == num[::-1] else False
5        