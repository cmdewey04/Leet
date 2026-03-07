# Last updated: 3/7/2026, 11:10:41 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        counts = Counter()
4        longest = 0
5        l = 0
6        for r in range(len(s)):
7            counts[s[r]]+=1
8            while (r-l+1) - max(counts.values()) > k:
9                counts[s[l]]-=1
10                if counts[s[l]]==0:
11                    del counts[s[l]]
12                l+=1
13            longest = max(longest, r-l+1)
14        return longest