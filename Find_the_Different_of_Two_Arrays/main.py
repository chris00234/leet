class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        tmp = []
        for i in set1:
            if i not in set2:
                tmp.append(i)
        res.append(tmp)
        tmp = []
        for j in set2:
            if j not in set1:
                tmp.append(j)
        res.append(tmp)
        return res