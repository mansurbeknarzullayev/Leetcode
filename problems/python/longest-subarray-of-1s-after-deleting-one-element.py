class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pref = [nums[i] for i in range(n)]
        suff = [nums[i] for i in range(n)]
        for i in range(1, n):
            if pref[i] > 0:
                pref[i] += pref[i - 1]
        for i in range(n - 2, -1, -1):
            if suff[i] > 0:
                suff[i] += suff[i + 1]
        for i in range(n):
            val = 0
            if i > 0:
                val += pref[i - 1]
            if i + 1 < n:
                val += suff[i + 1]
            ans = max(ans, val)
        return ans