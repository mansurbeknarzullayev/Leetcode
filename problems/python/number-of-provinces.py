class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        g = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    g[i].append(j)
        used = [False for i in range(n)]
        ans = 0
        def go(v):
            used[v] = True
            for w in g[v]:
                if not used[w]:
                    go(w)
        
        for i in range(n):
            if not used[i]:
                ans += 1
                go(i)
        return ans