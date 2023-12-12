class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        sum, cnt, ind = 0, 0, 0
        for x in nums:
            sum += x
            cnt += 1
            while sum >= target:
                ans = min(ans, cnt)
                sum -= nums[ind]
                ind += 1
                cnt -= 1
        return ans if ans <= len(nums) else 0