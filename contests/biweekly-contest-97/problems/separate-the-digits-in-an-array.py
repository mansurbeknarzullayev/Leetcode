class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []
        for x in nums:
            s = str(x)
            for c in s:
                ret.append(int(c))
        return ret