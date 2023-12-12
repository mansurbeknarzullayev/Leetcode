class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        ll = [0 for i in range(n)]
        rr = [0 for i in range(n)]

        ind = 0
        ans = 0
        for i in range(n):
            x = prizePositions[i]

            while x - prizePositions[ind] > k:
                ind += 1
            if i > 0:
                ll[i] = ll[i - 1]
            ll[i] = max(ll[i], i - ind + 1)

        ind = n - 1
        for i in range(n - 1, -1, -1):
            x = prizePositions[i]

            while prizePositions[ind] - x > k:
                ind -= 1
            if i + 1 < n:
                rr[i] = rr[i + 1]

            rr[i] = max(rr[i], ind - i + 1)

        for i in range(n):
            tmp = ll[i]
            if i + 1 < n:
                tmp += rr[i + 1]
            ans = max(ans, tmp)
        return ans

