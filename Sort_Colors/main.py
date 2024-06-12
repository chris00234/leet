class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        two = len(nums) - 1
        curr = 0

        while curr <= two:
            if nums[curr] == 0:
                nums[curr], nums[zero] = nums[zero], nums[curr]
                zero += 1
                if curr < zero :
                    curr = zero
            elif nums[curr] == 2:
                nums[curr], nums[two] = nums[two], nums[curr]
                two -= 1
            else:
                curr += 1
