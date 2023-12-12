class Solution:
    def floodFill(self, a: List[List[int]], sr: int, sc: int, c: int) -> List[List[int]]:
        global used
        used = [[0 for i in range(len(a[0]))] for j in range(len(a))]

        def go(x, y, c):
            global used
            if a[x][y] == c:
                used[x][y] = 1
            else:
                used[x][y] = -1
            val = a[x][y]
            if x + 1 < len(a) and a[x + 1][y] == val and used[x + 1][y] == 0:
                go(x + 1, y, c)
            if x - 1 >= 0 and a[x - 1][y] == val and used[x - 1][y] == 0:
                go(x - 1, y, c)
            if y + 1 < len(a[0]) and a[x][y + 1] == val and used[x][y + 1] == 0:
                go(x, y + 1, c)
            if y - 1 >= 0 and a[x][y - 1] == val and used[x][y - 1] == 0:
                go(x, y - 1, c)

        go(sr, sc, a[sr][sc])
        print(*used, sep='\n')
        for i in range(len(a)):
            for j in range(len(a[0])):
                if used[i][j] == 1:
                    a[i][j] = c
        return a