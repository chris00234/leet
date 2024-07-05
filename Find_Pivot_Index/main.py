class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        prefix = 0
        suffix = sum(nums[1:])
        i = 0
        for i in range(len(nums) - 1):
            if prefix == suffix:
                return i
            prefix += nums[i]
            suffix -= nums[i + 1]
        if prefix == suffix:
            return i + 1
        return -1


