class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = sum(nums[:3])
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                need = target - nums[i] - nums[j]
                pos = bisect.bisect_left(nums, need)
                p = pos
                while p == i or p == j:
                    p -= 1
                if 0 <= p < n and abs(ans - target) > abs(nums[i] + nums[j] + nums[p] - target):
                    ans = nums[i] + nums[j] + nums[p]
                
                p = pos - 1
                while p == i or p == j:
                    p -= 1
                if 0 <= p < n and abs(ans - target) > abs(nums[i] + nums[j] + nums[p] - target):
                    ans = nums[i] + nums[j] + nums[p]
                
                p = pos + 1
                while p == i or p == j:
                    p += 1
                if 0 <= p < n and abs(ans - target) > abs(nums[i] + nums[j] + nums[p] - target):
                    ans = nums[i] + nums[j] + nums[p]
        return ans