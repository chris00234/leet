class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        dic2 = {}

        for num in nums1:
            dic1[num] = dic1.get(num, 0) + 1
        for num in nums2:
            dic2[num] = dic2.get(num, 0) + 1
        ret = []
        for key in dic1:
            if key in dic2:
                val = min(dic1[key], dic2[key])
                for i in range(val):
                    ret.append(key)
        return ret
