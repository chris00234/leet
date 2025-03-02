class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}

        for num in nums1:
            dic[num[0]] = dic.get(num[0], 0) + num[1]

        for num in nums2:
            dic[num[0]] = dic.get(num[0], 0) + num[1]

        return sorted([[key, value] for key, value in dic.items()])
