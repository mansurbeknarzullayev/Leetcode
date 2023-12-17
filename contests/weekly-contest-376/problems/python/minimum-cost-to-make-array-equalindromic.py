class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pv = [i for i in range(1, 10)]
        deg = 1
        mx = nums[-1]
        for i in range(1, 10000):
            if i % deg == 0:
                deg *= 10
            s = str(i)
            v2 = int(s[::-1])
            pv.append(i * deg + v2)
            for j in range(10):
                pv.append((i * 10 + j) * deg + v2)
            if i * deg > mx:
                break
        pv = list(set(pv))
        pv.sort()
        pos = 0
        sm = sum(nums)
        ans = sm - 1
        s = sm
        l = 0
        print(len(pv))
        for x in pv:
            while pos < n and nums[pos] < x:
                l += nums[pos]
                s -= nums[pos]
                pos += 1
            if pos < n:
                ans = min(ans, x * pos - l + s - (n - pos) * x)
            else:
                ans = min(ans, x * n - sm)
                break
        return ans
            
                