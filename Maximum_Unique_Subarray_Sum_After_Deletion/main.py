class Solution:
    def maxSum(self, nums: List[int]) -> int:
        minimizedList = list(set(nums))
        ret = 0
        if len(minimizedList) == 1:
            return minimizedList[0]
        for i in range(len(minimizedList)):
            if minimizedList[i] > 0:
                ret += minimizedList[i]
            if i == (len(minimizedList) - 1) and ret == 0:
                ret = max(minimizedList)
        return ret
