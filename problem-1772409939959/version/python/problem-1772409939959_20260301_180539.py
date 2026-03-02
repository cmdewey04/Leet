# Last updated: 3/1/2026, 6:05:39 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        # seen = set()
4        # longest = 0
5        # current = 0
6        # for i in range(len(s)):
7        #     current = 1
8        #     seen.add(s[i])
9        #     for j in range(i+1, len(s)):
10        #         if s[j] not in seen:
11        #             seen.add(s[j])
12        #             current+=1
13        #             longest = max(longest, current)
14        #         else:
15        #             longest = max(longest, current)
16        #             current = 0
17        #             seen.clear()
18        #             break
19        # return max(longest, current)
20
21
22        seen = set()
23        longest = 0
24        current = 0
25        for i in range(len(s)):
26            seen.add(s[i])
27            current = 1
28            r=i+1
29            while r<len(s):
30                if s[r] not in seen:
31                    seen.add(s[r])
32                    current+=1
33                    longest = max(longest, current)
34                    r+=1
35                else:
36                    longest = max(longest, current)
37                    current=0
38                    seen.clear()
39                    break
40        return max(longest, current)