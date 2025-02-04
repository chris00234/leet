class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = nums[0]
        mx = prev
        sm = prev

        for i in range(1, len(nums)):
            if prev < nums[i]:
                sm += nums[i]
            else:
                sm = nums[i]
            mx = max(sm, mx)
            prev = nums[i]
        return mx
