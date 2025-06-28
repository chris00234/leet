class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        numCopy = nums.copy()
        nums.sort()
        tmp = []
        ret = []
        for i in range(len(nums) - 1, len(nums) - 1 - k, -1):
            tmp.append(nums[i])
        
        for num in numCopy:
            if num in tmp:
                ret.append(num)
                idx = tmp.index(num)
                tmp.pop(idx)
        return ret

