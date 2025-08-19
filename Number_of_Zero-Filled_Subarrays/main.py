class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        idx = 0
        ret = 0
        while idx < len(nums):
            if nums[idx] == 0:
                while idx < len(nums) and nums[idx] == 0:
                    zeros += 1
                    idx += 1
            else:
                idx += 1
            ret += ((zeros * (zeros + 1))/2)
            zeros = 0
        return int(ret)
