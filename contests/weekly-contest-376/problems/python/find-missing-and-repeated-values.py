class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a = 0
        b = 0
        cnt = [0 for i in range(n * n + 1)]
        for v in grid:
            for x in v:
                cnt[x] += 1
        for i in range(1, n * n + 1):
            if cnt[i] == 0:
                a = i
            if cnt[i] == 2:
                b = i
        return [b, a]