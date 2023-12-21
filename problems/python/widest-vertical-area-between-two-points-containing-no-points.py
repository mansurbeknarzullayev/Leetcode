class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for i in range(len(points)):
            if i > 0:
                ans = max(ans, points[i][0] - points[i - 1][0])
        return ans