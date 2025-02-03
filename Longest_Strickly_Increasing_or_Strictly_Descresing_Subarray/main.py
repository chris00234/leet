class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        mx = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                inc += 1
                dec = 1
            elif nums[i] < prev:
                inc = 1
                dec += 1
            else:
                inc = 1
                dec = 1
            prev = nums[i]
            mx = max(inc, dec, mx)
        return mx
