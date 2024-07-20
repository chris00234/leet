class Solution:
    def restoreMatrix(self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= dp[i][j]
                colSum[j] -= dp[i][j]

        return dp
