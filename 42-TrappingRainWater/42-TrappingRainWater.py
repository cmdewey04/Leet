# Last updated: 2/26/2026, 1:36:54 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        #use two pointers starting at 0 and len-1
        #use a maxL and maxR to keep track of while side has the max at a time (elimainating need for prefix/suffix arrays)
        #move towards min of the max each time
        l,r = 0, len(height)-1
        total = 0
        maxL = height[l]
        maxR = height[r]
        while l<r:
            if maxL < maxR:
                l+=1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                total += maxR - height[r]
        
        return total

        