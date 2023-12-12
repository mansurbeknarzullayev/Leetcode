class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        k = len(nums) - k
        while k > 0:
            nums.append(nums[0])
            nums.pop(0)
            k -= 1