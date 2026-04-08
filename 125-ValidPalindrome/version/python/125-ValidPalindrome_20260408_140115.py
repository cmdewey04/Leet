# Last updated: 4/8/2026, 2:01:15 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        clean = "".join(char for char in s if char.isalnum())
4        clean_lower = clean.lower()
5        check = clean_lower[::-1]
6        if check == clean_lower:
7            return True
8        return False
9
10        