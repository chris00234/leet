class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in range(length)]

        for i in range(length):
            for j in range(1, nums[i] + 1):
                if i + j < length:
                    if dp[i + j] != 0 and dp[i + j] < dp[i] + 1:
                        pass
                    else:
                        dp[i + j] = dp[i] + 1
        
        return dp[-1]