class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l = 0
        r = 10 ** 9 + 1
        while r - l > 1:
            m = (l + r) // 2
            cnt = 0
            old = -2
            for i in range(len(nums)):
                if nums[i] <= m and i - old > 1:
                    cnt += 1
                    old = i
            if cnt >= k:
                r = m
            else:
                l = m
        return r