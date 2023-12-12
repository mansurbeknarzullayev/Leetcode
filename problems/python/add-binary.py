class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        rem = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or rem > 0:
            s = rem
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            ans = str(s % 2) + ans
            rem = s // 2
        return ans if ans != '' else '0'
