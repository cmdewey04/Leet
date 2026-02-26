# Last updated: 2/26/2026, 1:36:51 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        l,r = 0, len(matrix) -1
        first,last = 0, len(matrix[0])-1
        col = last

        #If not a match there are 3 possible cases
        #Case 1: In the same array
        #       - left and right need to be that array
        #       - we dec/inc the el count
        #Case 2: In array to the left
        #       - shift r to midMat - 1
        #Case 3: In array to the right
        #       - shift l to midMat + 1




        while l<=r and first<=last:
            midMat = (l+r)//2
            midEl = (first+last)//2
            if matrix[midMat][midEl] == target:
                return True
            elif matrix[midMat][midEl] > target:
                #Check if an array
                if matrix[midMat][0] <= target:
                    l = midMat
                    r = midMat
                    last = midEl - 1
                else:
                    r = midMat - 1
            else:
                #Check if in array
                if matrix[midMat][col] >= target:
                    l = midMat
                    r = midMat
                    first = midEl + 1
                else:
                    l = midMat + 1
        return False
        