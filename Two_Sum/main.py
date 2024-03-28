class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        n = len(nums)

        for i in range(n):
            subtract = target - nums[i]
            if subtract in mp:
                return [mp[subtract], i]
            mp[nums[i]] = i

        return mp
