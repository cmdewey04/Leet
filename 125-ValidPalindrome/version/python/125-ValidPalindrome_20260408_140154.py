# Last updated: 4/8/2026, 2:01:54 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        clean = "".join(char for char in s if char.isalnum())
4        clean_lower = clean.lower()
5        if clean_lower == clean_lower[::-1]:
6            return True
7        return False
8
9        