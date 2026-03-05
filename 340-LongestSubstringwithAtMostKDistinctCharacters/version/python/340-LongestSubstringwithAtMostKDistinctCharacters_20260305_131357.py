# Last updated: 3/5/2026, 1:13:57 PM
1class Solution:
2    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
3        if k == 0:
4            return 0
5
6        count = Counter()
7        longest = 0
8        l = 0
9        for r in range(len(s)):
10            count.update(s[r])
11            #If adding new element makes Count go above k
12            while len(count) > k:
13                count[s[l]] -= 1
14                if count[s[l]] == 0:
15                    del count[s[l]]
16                l+=1
17            longest = max(longest, r-l+1) 
18        return longest
19
20        