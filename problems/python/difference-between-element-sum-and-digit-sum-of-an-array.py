class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = 0
        digit_sum = 0
        for x in nums:
            el_sum += x
            while x > 0:
                digit_sum += x % 10
                x //= 10
        return abs(el_sum - digit_sum)