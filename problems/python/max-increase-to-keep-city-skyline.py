class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mc = [0 for i in range(m)]
        mr = [0 for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                mc[j] = max(mc[j], grid[i][j])
                mr[i] = max(mr[i], grid[i][j])
        for i in range(n):
            for j in range(m):
                ans += min(mr[i], mc[j]) - grid[i][j]
        return ans