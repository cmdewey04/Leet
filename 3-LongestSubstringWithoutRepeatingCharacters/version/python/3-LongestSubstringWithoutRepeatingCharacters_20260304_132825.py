# Last updated: 3/4/2026, 1:28:25 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        longest = 0
5        l = 0
6
7        for r in range(len(s)):
8            while s[r] in seen:
9                seen.remove(s[l])
10                l+=1
11            longest = max(longest, r-l+1)
12            seen.add(s[r])
13        return longest
14
15
16            