class Solution:
    def tribonacci(self, n: int) -> int:
        vec = [0 for i in range(max(n + 1, 5))]
        vec[1] = 1
        vec[2] = 1
        for i in range(3, n + 1):
            vec[i] = vec[i - 1] + vec[i - 2] + vec[i - 3]
        return vec[n]