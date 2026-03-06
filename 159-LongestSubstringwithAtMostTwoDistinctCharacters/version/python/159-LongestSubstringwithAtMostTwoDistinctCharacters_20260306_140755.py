# Last updated: 3/6/2026, 2:07:55 PM
1class Solution:
2    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
3        count = Counter()
4        longest = 0
5        l = 0
6        for r in range(len(s)):
7            count[s[r]]+=1
8            while len(count) > 2:
9                count[s[l]]-=1
10                if count[s[l]]==0:
11                    del count[s[l]]
12                l+=1
13            longest=max(longest, r-l+1)
14        return longest