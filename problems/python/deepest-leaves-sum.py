# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth = 0

        def go(node, d):
            if node:
                if d == self.depth:
                    self.ans += node.val
                elif d > self.depth:
                    self.depth = d
                    self.ans = node.val

                go(node.left, d + 1)
                go(node.right, d + 1)

        go(root, 0)
        return self.ans