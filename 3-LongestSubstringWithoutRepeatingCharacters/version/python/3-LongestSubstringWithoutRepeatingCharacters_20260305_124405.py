# Last updated: 3/5/2026, 12:44:05 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        longest = 0
5        l = 0
6        current = 0
7        for r in range(len(s)):
8            while s[r] in seen:
9                longest = max(longest, r-l)
10                seen.remove(s[l])
11                l+=1
12            seen.add(s[r])
13            longest = max(longest, r-l+1)
14        return longest
15
16
17            