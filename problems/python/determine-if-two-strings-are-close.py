class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = [0 for i in range(26)]
        cnt2 = [0 for i in range(26)]

        for c in word1:
            cnt1[ord(c) - ord('a')] += 1
        for c in word2:
            cnt2[ord(c) - ord('a')] += 1
        v1 = [1]
        v2 = [1]
        for i in range(26):
            if cnt1[i] != cnt2[i]:
                v1.append(cnt1[i])
                v2.append(cnt2[i])
        v1.sort()
        v2.sort()
        return v1[0] > 0 and v2[0] > 0 and v1 == v2