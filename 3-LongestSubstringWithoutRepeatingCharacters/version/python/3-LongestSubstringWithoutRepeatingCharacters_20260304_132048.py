# Last updated: 3/4/2026, 1:20:48 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        longest = 0
5        r = 0
6        current=0
7        for l in range(len(s)):
8            # if s[r] in seen:
9            #     longest = max(longest, r-l+1)
10            #     seen.remove(s[r])
11            #     l+=1
12            #     r-=1
13            # else:
14            #     seen.add(s[r])
15            seen.add(s[l])
16            current=1
17            r=l+1
18            while r < len(s):
19                if s[r] not in seen:
20                    current+=1
21                    longest = max(longest, current)
22                    seen.add(s[r])
23                    r+=1
24                else:
25                    longest = max(longest, current)
26                    seen.clear()
27                    break
28        return max(longest, current)
29            