# Last updated: 2/26/2026, 1:36:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def bfs(node, sumT):
            if not node:
                return False
            sumT += node.val
            if sumT == targetSum:
                if not node.left and not node.right:
                    return True
            return (bfs(node.left,sumT) or bfs(node.right,sumT))
        return bfs(root,0)
            

        