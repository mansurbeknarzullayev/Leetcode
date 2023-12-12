class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = 0
        for i in range(len(s)):
            sz = 0
            while 0 <= i - sz and i + sz < len(s):
                if s[i - sz] == s[i + sz]:
                    sz += 1
                else:
                    break
            if r - l + 1 < 2 * sz - 1:
                l = i - sz + 1
                r = i + sz - 1

            if i + 1 < len(s) and s[i] == s[i + 1]:
                sz = 0
                while 0 <= i - sz and i + sz + 1 < len(s):
                    if s[i - sz] == s[i + sz + 1]:
                        sz += 1
                    else:
                        break
                if r - l + 1 < 2 * sz:
                    l = i - sz + 1
                    r = i + sz

        return s[l:r + 1]