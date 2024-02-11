class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            nums[:] = [nums[-1]] + nums[:-1]
        
            


ans = Solution()
nums = [1,2,3,4,5,6,7]
ans.rotate(nums, 3)
print(nums)