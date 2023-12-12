# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r