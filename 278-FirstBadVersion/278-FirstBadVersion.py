# Last updated: 2/26/2026, 1:36:32 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1, n
        while l < r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
        