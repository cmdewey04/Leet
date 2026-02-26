# Last updated: 2/26/2026, 1:36:29 PM
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        #recursion
        #Loop through the array and call bfs on the element/list
        #keep a sumTotal
        #if isInteger outside of recursive func, add 1 * value
        #recursive func params: list, depth
            #loops through the array, if isInt, add depth * value
            #else call recursive func again on that list element with incremented depth

       
        total = 0

        def bfs(nestedList, depth, listSum):
            for nDx in range(len(nestedList)):
                if nestedList[nDx].isInteger():
                    listSum += depth * nestedList[nDx].getInteger()
                    continue
                listSum = bfs(nestedList[nDx].getList(), depth+1, listSum)
            return listSum
                    


        
        for el in range(len(nestedList)):
            if nestedList[el].isInteger():
                total += nestedList[el].getInteger()
                continue
            total = bfs(nestedList[el].getList(), 2, total)

        return total