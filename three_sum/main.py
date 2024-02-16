class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif  sum < 0:
                    l += 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return result

        #-4 -1 -1 0 1 2