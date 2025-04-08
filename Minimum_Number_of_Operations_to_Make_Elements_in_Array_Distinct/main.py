class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ret = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                return ret
            nums = nums[3:]
            ret += 1
        return ret

