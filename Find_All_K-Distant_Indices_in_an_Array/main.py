class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret = []
        idx = []

        for i in range(len(nums)):
            if nums[i] == key:
                idx.append(i)

        for i in idx:
            for j in range(len(nums)):
                if abs(i - j) <= k:
                    ret.append(j)
        return list(set(ret))

