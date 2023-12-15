class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -20 ** 10
        s = 0
        n = len(nums)
        for i in range(n):
            s += nums[i]
            if i >= k:
                s -= nums[i - k]
            if i + 1 >= k:
                ans = max(ans, s / k)
            
        return ans