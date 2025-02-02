class Solution:
    def check(self, nums: List[int]) -> bool:
        prev = nums[0]
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] < prev:
                pos = i
                break
            prev = nums[i]
        tmp = nums[pos:] + nums[:pos]
        nums.sort()
        if tmp == nums:
            return True
        return False
