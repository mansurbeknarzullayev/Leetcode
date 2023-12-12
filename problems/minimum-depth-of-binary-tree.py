class Solution:
    def go(self, t: TreeNode, h: int):
        if t != None:
            if t.left != None or t.right != None:
                if t.left != None:
                    self.go(t.left, h + 1)
                if t.right != None:
                    self.go(t.right, h + 1)
            else:
                self.mn = min(self.mn, h + 1)
        else:
            self.mn = min(self.mn, h)
    def minDepth(self, root: TreeNode) -> int:
        self.mn = 10 ** 10
        self.go(root, 0)
        if root == None:
            self.mn = 0
        return self.mn
        