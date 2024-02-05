class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == current_num:
                nums = nums[0:i] + nums[i + 1:] + ['_']
                current_num = nums[i]
            else:
                current_num = nums[i]

        return nums
                

ans = Solution()
nums = [1,1,2,2,3,3,4,4,5,5]
print(ans.removeDuplicates(nums))