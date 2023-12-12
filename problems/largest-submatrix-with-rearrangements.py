class Solution:
    def largestSubmatrix(self, a: List[List[int]]) -> int:
        n = len(a)
        m = len(a[0])
        d = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                d[i][j] = a[i][j]
                if d[i][j] > 0 and i > 0:
                    d[i][j] += d[i - 1][j]
        
        ans = 0
        for i in range(n):
            d[i].sort(reverse=True)
            for j in range(m):
                ans = max(ans, d[i][j] * (j + 1))
        return ans