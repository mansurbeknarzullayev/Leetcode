class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, n):
                        if nums[k] - nums[j] == diff:
                            ans += 1
                        elif nums[k] - nums[j] > diff:
                            break
                elif nums[j] - nums[i] > diff:
                    break
        return ans