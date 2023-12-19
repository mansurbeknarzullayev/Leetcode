# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.d = {}
        def go(node, dep):
            if node:
                if not(dep in self.d):
                    self.d[dep] = 0
                self.d[dep] += node.val
                go(node.left, dep + 1)
                go(node.right, dep + 1)

        go(root, 0)
        ans = 0
        for x in self.d:
            if self.d[ans] < self.d[x]:
                ans = x
        return ans + 1