class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        v = []
        for x in arr:
            v.append([x.bit_count(), x])
        v.sort()
        return [x[1] for x in v]
