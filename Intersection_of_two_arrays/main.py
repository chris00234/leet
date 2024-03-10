class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        result = []
        nums1.sort()
        nums2.sort()

        if nums1[-1] < nums2[0]:
            return []
        if nums2[-1] < nums1[0]:
            return []

        for i in nums1:
            for j in nums2:
                if i < j:
                    break
                elif i == j:
                    result.append(i)
        return result