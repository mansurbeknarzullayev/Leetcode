class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz = 0
        if len(strs) > 0:
            sz = min(list(map(lambda x: len(x), strs)))
        ret = ''
        for i in range(sz):
            ok = True
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    ok = False
            if ok:
                ret += strs[0][i]
            else:
                break
        return ret