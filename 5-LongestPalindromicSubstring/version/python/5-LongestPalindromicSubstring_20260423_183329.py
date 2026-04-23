# Last updated: 4/23/2026, 6:33:29 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        biggest = 0
4        word = ""
5        for i in range(len(s)):
6            #odd length
7            l,r = i,i 
8            while l >= 0 and r < len(s) and s[l] == s[r]:
9                if (r-l+1) > biggest:
10                    biggest = r-l+1
11                    word = s[l:r+1]
12                l-=1
13                r+=1
14            
15            #even length
16            l,r = i, i+1
17            while l >= 0 and r < len(s) and s[l] == s[r]:
18                if (r-l+1) > biggest:
19                    biggest = r-l+1
20                    word = s[l:r+1] 
21                l-=1
22                r+=1
23        return word
24
25        
26                