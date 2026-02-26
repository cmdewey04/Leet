# Last updated: 2/26/2026, 1:37:01 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        current = 0
        for i in range(len(s)):
            current = 1
            seen.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    current+=1
                    longest = max(longest, current)
                else:
                    longest = max(longest, current)
                    current = 0
                    seen.clear()
                    break
        return max(longest, current)
        