class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        st = [set() for i in range(26)]
        ans = 0
        for name in ideas:
            st[ord(name[0]) - ord('a')].add(name[1:])
        for i in range(26):
            for j in range(i + 1, 26):
                v = (st[i] & st[j])
                ans += 2 * (len(st[i]) - len(v)) * (len(st[j]) - len(v))
        return ans