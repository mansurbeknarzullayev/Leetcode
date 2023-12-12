class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num + 1
        while r - l > 1:
            m = (l + r) // 2
            if m * m <= num:
                l = m
            else:
                r = m
        return l * l == num