class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = len(nums)
        count = 0
        for x in range(len(nums), -1, -1):
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return x
            else:
                count = 0
        return -1
