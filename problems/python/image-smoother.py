class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        res = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                s = 0
                cnt = 0
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if 0 <= i + ii < n and 0 <= j + jj < m:
                            s += img[i + ii][j + jj]
                            cnt += 1
                res[i][j] = s // cnt
        return res