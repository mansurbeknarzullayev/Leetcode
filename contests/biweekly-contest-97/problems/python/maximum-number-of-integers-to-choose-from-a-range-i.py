class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = list(set(banned))
        banned.sort()
        ind = 0
        ans = 0
        for i in range(1, n + 1):
            if ind < len(banned):
                if banned[ind] == i:
                    ind += 1
                elif maxSum >= i:
                    maxSum -= i
                    ans += 1
            elif maxSum >= i:
                maxSum -= i
                ans += 1
        return ans