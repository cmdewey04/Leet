# Last updated: 3/6/2026, 1:39:45 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        seen = Counter()
4        longest = 0
5        l = 0
6        for r in range(len(s)):
7            #Valid - increment toREplace logic
8            seen[s[r]]+=1
9            replacements_needed = (r-l+1) - max(seen.values())
10            while replacements_needed > k:
11                seen[s[l]]-=1
12                l+=1
13                replacements_needed = (r-l+1) - max(seen.values())
14            #Valid
15            longest = max(longest, r-l+1)
16        return longest