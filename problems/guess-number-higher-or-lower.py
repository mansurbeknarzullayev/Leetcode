class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n + 1
        while r - l > 1:
            pick = (l + r) // 2
            if guess(pick) > -1:
                l = pick
            else:
                r = pick
        return l