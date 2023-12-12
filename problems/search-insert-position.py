class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        if nums[l] >= target:
            return l
        else:
            return l + 1