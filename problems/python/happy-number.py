class Solution:
    def isHappy(self, n: int) -> bool:
        iter = 0
        while iter < 100 and n > 1:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            n = s
            iter += 1
        return n == 1