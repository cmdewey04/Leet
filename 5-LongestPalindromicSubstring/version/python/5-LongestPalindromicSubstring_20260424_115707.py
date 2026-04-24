# Last updated: 4/24/2026, 11:57:07 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest = 0
4        word = ""
5
6        for i in range(len(s)):
7            
8            #odd cases
9            l,r = i,i
10            while l >= 0 and r < len(s) and s[l] == s[r]:
11                if (r-l+1) > longest:
12                    longest = r-l+1
13                    word = s[l:r+1]
14                l-=1
15                r+=1
16            
17            #even cases
18            l,r = i, i+1
19            while l >= 0 and r < len(s) and s[l] == s[r]:
20                if (r-l+1) > longest:
21                    longest = r-l+1
22                    word = s[l:r+1]
23                l-=1
24                r+=1
25
26        return word
27