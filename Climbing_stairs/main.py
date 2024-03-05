class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for i in range(n + 1)]

        for i in range(n + 1):
            if i < 3:
                memo[i] = i
            else:
                memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

        

        
