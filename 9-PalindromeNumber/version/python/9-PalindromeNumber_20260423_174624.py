# Last updated: 4/23/2026, 5:46:24 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        return True if str(x) == str(x)[::-1] else False
4        