class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ret += 1
        return ret if len(nums) == sum(nums) else -1
