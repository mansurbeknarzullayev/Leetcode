class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        size = 0
        used = [False for i in range(n)]
        def go(v):
            used[v] = True
            for x in isConnected[v]:
                if x > 0 and not used[x]:
                    go(x)
        for i in range(n):
            if not used[i]:
                go(i)
                size += 1
        return size