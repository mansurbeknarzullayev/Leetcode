class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = {}
        ds = {}
        for i in range(26):
            dp[chr(i + ord('a'))] = 0
            ds[chr(i + ord('a'))] = 0
        ret = []
        for c in p:
            if c in dp:
                dp[c] += 1
        ns = len(s)
        np = len(p)
        for i in range(ns):
            ds[s[i]] += 1
            if ds == dp:
                ret.append(i - np + 1)
            if i + 1 >= np:
                ds[s[i - np + 1]] -= 1
        return ret