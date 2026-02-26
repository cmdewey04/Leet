# Last updated: 2/26/2026, 1:36:58 PM
class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)%2 != 0: return False

        # stack = []
        # pairs = { ")" : "(", "]" : "[", "}" : "{"}

        # for c in s:
        #     if c in pairs:
        #         if stack and stack[-1] == pairs[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return True if not stack else False


        if len(s) % 2 != 0: return False

        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in closeToOpen:
                #closing bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False