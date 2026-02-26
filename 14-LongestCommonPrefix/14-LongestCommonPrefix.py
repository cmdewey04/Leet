# Last updated: 2/26/2026, 1:36:59 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the most common between first two
        #if third is less than that, shrink,
        #if third is more, keep the same -> continue to loop

        if len(strs) == 1:
            return strs[0]

        first = strs[0]
        second = strs[1]
        common = ""
        longest = len(first) if len(first) < len(second) else len(second)
        for i in range(0, longest):
            if first[i] == second[i]:
                common+=first[i]
            else: 
                break
        
        for i in range(2, len(strs)):
            for j in range(0, len(common)):
                try:
                    if strs[i][j] != common[j]:
                        common = common[:j]
                        break
                except IndexError:
                    common = common[:j]
                    break
        
        return common
                    
        

