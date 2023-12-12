class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) + 1
        while r - l > 1:
            m = (l + r) // 2
            if sum([(x + m - 1) // m for x in piles]) <= h:
                r = m
            else:
                l = m
        return r