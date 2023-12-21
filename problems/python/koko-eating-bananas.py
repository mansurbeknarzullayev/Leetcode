class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = 10 ** 10
        while r - l > 1:
            m = (l + r) // 2
            cnt = 0
            for x in piles:
                cnt += (x + m - 1) // m
            if cnt <= h:
                r = m
            else:
                l = m
        return r