# Last updated: 4/15/2026, 6:13:30 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        #if its a close bracket, need to verify that stack isnt empty and then pop and check that they match up
4        closeToOpen = {")":"(", "]":"[", "}":"{"}
5        stack = []
6        for char in s:
7            if char not in closeToOpen:
8                #Open bracket add to stack
9                stack.append(char)
10            else:
11                #Close bracket
12                if stack and closeToOpen[char] == stack.pop():
13                    continue
14                else:
15                    return False
16        return True if not stack else False 
17        