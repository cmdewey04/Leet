# Last updated: 2/26/2026, 1:36:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        def bfs(root,depth):
            depth+=1
            if not root.left and not root.right:
                return depth
            if not root.left and root.right:
                return bfs(root.right,depth)
            if root.left and not root.right:
                return bfs(root.left,depth)
            else: 
                return max(bfs(root.left,depth),bfs(root.right,depth))
        
        return(bfs(root,depth))
            
        