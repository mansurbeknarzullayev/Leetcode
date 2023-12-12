class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0:
            n += 2 ** 32
        ans = 0
        while n > 0:
            ans += n % 2
            n //= 2
        return ans