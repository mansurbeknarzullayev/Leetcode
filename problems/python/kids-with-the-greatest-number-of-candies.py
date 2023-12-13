class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        mx = max(candies)
        for x in candies:
            res.append(x + extraCandies >= mx)
        return res
