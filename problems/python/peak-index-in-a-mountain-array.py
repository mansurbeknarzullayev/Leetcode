class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        while r - l > 1:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m
            else:
                r = m
        return l + 1