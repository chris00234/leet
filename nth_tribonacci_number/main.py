class Solution:
    def tribonacci(self, n: int) -> int:
        memo = []
        memo.append(0)
        memo.append(1)
        memo.append(1)
        

        for i in range(3, n + 1):
            memo.append(memo[i -3] + memo[i - 2] + memo[i - 1])
        return memo[n]