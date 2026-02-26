# Last updated: 2/26/2026, 1:36:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left = False
        res = []
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            level = []
            for i in range(l):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left) 
            if level and not left:
                res.append(level[::-1])
            elif level:
                res.append(level)
            left = not left
        return res

        