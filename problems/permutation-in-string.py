class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        t = len(s1)
        c = [0 for i in range(26)]
        cnt = [0 for i in range(26)]
        ok = False
        for cc in s1:
            c[ord(cc) - ord('a')] += 1
        for i in range(n):
            cnt[ord(s2[i]) - ord('a')] += 1
            if i >= t:
                cnt[ord(s2[i - t]) - ord('a')] -= 1
            if cnt == c:
                ok = True
        return ok