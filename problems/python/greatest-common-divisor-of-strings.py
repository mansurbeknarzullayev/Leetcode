class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        n = len(str1)
        m = len(str2)
        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0 and str1[:i] * (n // i) == str1 and str1[:i] * (m // i) == str2:
                ans = str1[:i]
        return ans