class Solution:
    def maxProduct(self, a: List[int]) -> int:
        for i in range(len(a)):
            a[i] -= 1
        a.sort()
        return max(a[0] * a[1], a[-1] * a[-2])