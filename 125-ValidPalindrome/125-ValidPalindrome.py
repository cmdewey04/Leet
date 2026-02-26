# Last updated: 2/26/2026, 1:36:43 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        good = ""
        lower = s.lower()
        for var in lower:
            if var.isalnum():
                good += var
                
        if good == good[::-1]:
            return True
        return False


        