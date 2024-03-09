class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] < nums2[0] or nums1[0] > nums2[-1]:
            return -1
        i,j = 0, 0
            
        while True:
            if i == len(nums1) or j == len(nums2):
                break
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                return nums1[i]
        
        return -1
