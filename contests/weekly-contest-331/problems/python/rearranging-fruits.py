class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = {}
        mn1 = min(basket1)
        mn2 = min(basket2)

        mn = min(mn1, mn2)
        ans = 0
        for x in basket1:
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1

        for x in basket2:
            if x in cnt:
                cnt[x] -= 1
            else:
                cnt[x] = -1

        if mn1 < mn2:
            mx2 = -10 ** 10
            for x in cnt:
                if cnt[x] < 0:
                    mx2 = max(mx2, x)
            cnt[mn1] -= 2
            cnt[mx2] += 2
            ans += mn1
        elif mn1 > mn2:
            mx1 = -10 ** 10
            for x in cnt:
                if cnt[x] > 0:
                    mx1 = max(mx1, x)
            cnt[mx1] -= 2
            cnt[mn2] += 2
            ans += mn2

        v = []
        for x in cnt:
            if cnt[x] % 2 > 0:
                return -1
            if cnt[x] != 0:
                w = abs(cnt[x]) // 2

                for j in range(w):
                    v.append(x)

        v.sort()
        l = 0
        r = len(v) - 1
        while l < r:
            if v[l] < 2 * mn:
                ans += v[l]
            else:
                ans += 2 * mn
            l += 1
            r -= 1

        return ans