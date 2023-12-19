# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {}
        def go(node, dep):
            if node:
                if not(dep in self.d):
                    self.d[dep] = []
                self.d[dep].append(node.val)
                go(node.left, dep + 1)
                go(node.right, dep + 1)

        go(root, 0)
        res = []
        for x in self.d:
            if len(self.d) > 0:
                res.append(self.d[x][-1])
        return res