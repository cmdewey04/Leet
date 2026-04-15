# Last updated: 4/15/2026, 6:23:05 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        newS = ""
4        for char in s:
5            if char.isalnum():
6                newS += char.lower()
7        return newS == newS[::-1]
8
9        