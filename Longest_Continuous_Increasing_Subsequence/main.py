class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx = 0
        curr = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                curr += 1
            elif nums[i + 1] <= nums[i]:
                curr = 0
            
            if mx < curr:
                mx = curr
        return mx + 1
            
            
