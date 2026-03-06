# Last updated: 3/6/2026, 1:04:43 PM
1class Solution:
2    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
3        seen = Counter()
4        longest = 0
5        l = 0
6        for r in range(len(s)):
7            #add to Group
8            seen.update(s[r])
9            #Invalid Check
10            while len(seen) > k:
11                seen[s[l]]-=1
12                if seen[s[l]]==0:
13                    del seen[s[l]]
14                l+=1
15            #Valid by this point
16            longest = max(longest, r-l+1)
17        return longest