class Solution:
    def maxAreaOfIsland(self, a: List[List[int]]) -> int:
        ans = 0
        n = len(a)
        m = len(a[0])
        def go(x, y):
            ret = 0
            if a[x][y] == 1:
                ret += 1
            a[x][y] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((i == 0) ^ (j == 0)) == 1 and 0 <= x + i < n and 0 <= y + j < m and a[x + i][y + j] == 1:
                        ret += go(x + i, y + j)
            return ret
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    ans = max(ans, go(i, j))
        return ans