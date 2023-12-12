# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(r1, r2):
            ret = None
            if r1 and r2:
                ret = TreeNode(r1.val + r2.val)
                ret.left = merge(r1.left, r2.left)
                ret.right = merge(r1.right, r2.right)
            elif r1:
                ret = r1
            elif r2:
                ret = r2
            return ret

        return merge(root1, root2)