class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = sorted(list(set(nums)))
        ans = 0
        cnt = 0
        old = -10 ** 10
        for x in d:
            if x - old == 1:
                cnt += 1
            else:
                cnt = 1
            old = x
            ans = max(ans, cnt)
        return ans