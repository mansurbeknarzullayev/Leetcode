class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        if n % 3 > 0:
            return []
        else:
            for i in range(n):
                if i % 3 == 0:
                    ret.append([nums[i]])
                else:
                    ret[-1].append(nums[i])
        for i in range(len(ret)):
            if ret[i][2] - ret[i][0] > k:
                return []
        return ret