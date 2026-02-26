# Last updated: 2/26/2026, 1:36:41 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        new_string = s.split(" ")
        new_string.reverse()
        s = ""
        for var in new_string:
            if var != "":
                s += var + " "

        return s.strip()
        