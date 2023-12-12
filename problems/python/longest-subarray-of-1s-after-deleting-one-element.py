class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        arr = []
        for x in nums:
            if x > 0:
                cnt += 1
            else:
                arr.append(cnt)
                cnt = 0
        arr.append(cnt)
        ans = arr[0]
        for i in range(1, len(arr)):
            ans = max(ans, arr[i] + arr[i - 1])
        
        if sum(nums) == ans and not (0 in nums):
            ans -= 1
        return ans