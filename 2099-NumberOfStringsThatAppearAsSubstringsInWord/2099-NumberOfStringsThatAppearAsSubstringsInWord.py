# Last updated: 2/26/2026, 1:36:22 PM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for sub in patterns:
            if sub in word:
                count+=1

        return count
        