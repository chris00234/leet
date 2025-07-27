class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        ret = 0
        while i < (len(nums) - 1):
            curr = nums[i]
            before = nums[i - 1]
            for tmp in range(i + 1, len(nums)):
                if nums[tmp] != curr:
                    i = tmp - 1
                    break
            after = nums[i + 1]
            if (curr < before and curr < after) or (curr > before and curr > after):
                ret += 1
            i += 1
        return ret
            

