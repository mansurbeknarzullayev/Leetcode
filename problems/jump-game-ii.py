class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [10 ** 5 for i in range(n)]
        cnt[0] = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] >= j - i:
                    cnt[j] = min(cnt[j], cnt[i] + 1)
                else:
                    break
        return cnt[n - 1]