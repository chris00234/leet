class Solution:
    def canJump(self, nums: list[int]) -> bool:
        tmp = 0
        for i in nums:
            if tmp < 0:
                return False
            elif i > tmp:
                tmp = i
            tmp -= 1
        return True
    
    def canJump_dp(self, nums: list[int]) -> bool:
        length = len(nums)
        dp = [False for i in range(length)]
        dp[0] = True
        
        for i in range(length - 1):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < length:
                        dp[i + j] = True
                    elif i + j == length:
                        return True
        
        return dp[length - 1]
                