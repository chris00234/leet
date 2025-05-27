class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = []
        nums2 = []

        for i in range(1, n + 1):
            if i % m != 0:
                nums1.append(i)
            else:
                nums2.append(i)
        return sum(nums1) - sum(nums2)
