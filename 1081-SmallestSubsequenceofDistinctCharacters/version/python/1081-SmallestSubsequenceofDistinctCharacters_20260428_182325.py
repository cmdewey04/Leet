# Last updated: 4/28/2026, 6:23:25 PM
1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        stack = []
4        seen = set()
5        count = Counter(s)
6
7        occurences = {char:nDx for nDx, char in enumerate(s)}
8
9        for nDx,char in enumerate(s):
10            # if count[char] % 2 == 0:
11            #     continue
12            if char in seen:
13                continue
14            while stack and char < stack[-1] and nDx < occurences[stack[-1]]:
15                seen.discard(stack.pop())
16            seen.add(char)
17            stack.append(char)
18        return ''.join(stack)
19
20
21        