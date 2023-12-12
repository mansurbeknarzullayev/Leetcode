class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        cnt = [0 for i in range(len(words))]
        vv = ['a', 'e', 'o', 'i', 'u']
        for i in range(len(words)):
            if i > 0:
                cnt[i] += cnt[i - 1]
            if (words[i][0] in vv) and (words[i][-1] in vv):
                cnt[i] += 1
        ans = [0 for i in range(len(queries))]
        for i in range(len(queries)):
            ans[i] += cnt[queries[i][1]]
            if queries[i][0] > 0:
                ans[i] -= cnt[queries[i][0] - 1]
        return ans