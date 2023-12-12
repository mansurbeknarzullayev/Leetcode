class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        t = ''
        d = {}
        ind = 0
        for i in range(len(s)):
            t += s[i]
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            while d[s[i]] > 1:
                d[t[0]] -= 1
                t = t[1:]
            ans = max(ans, len(t))
        return ans