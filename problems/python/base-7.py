class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = 1
        if num < 0:
            sign = -1
            num = -num
        ans = 0
        p = 1
        while num > 0:
            ans += p * (num % 7)
            num //= 7
            p *= 10
        return str(sign * ans)