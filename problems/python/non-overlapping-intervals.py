class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = -10 ** 10
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        
        return ans