class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        while k > 0:
            k -= 1
            w = int(gifts[-1] ** 0.5)
            gifts.pop(-1)
            pos = bisect.bisect_left(gifts, w)
            gifts.insert(pos, w)
        return sum(gifts)
