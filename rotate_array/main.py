class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        nums[:] = nums[len(nums) - k :] + nums[:len(nums) - k]
        
            


ans = Solution()
nums = [1,2,3,4,5,6,7]
ans.rotate(nums, 3)
