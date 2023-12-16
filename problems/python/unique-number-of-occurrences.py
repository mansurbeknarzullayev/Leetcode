class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for x in arr:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        v = []
        for x in d:
            v.append(d[x])
        v.sort()
        for i in range(1, len(v)):
            if v[i] == v[i - 1]:
                return False
        return True