class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        v1 = []
        v2 = []
        for x in nums1:
            if not(x in nums2) and not(x in v1):
                v1.append(x)
        for x in nums2:
            if not(x in nums1) and not(x in v2):
                v2.append(x)
        return [v1, v2]