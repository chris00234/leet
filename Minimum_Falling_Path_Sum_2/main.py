class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for row in range(1, n):
            for col in range(n):
                if col == 0:
                    grid[row][col] = min(grid[row - 1][1:]) + grid[row][col]
                elif col == n - 1:
                    grid[row][col] = min(grid[row - 1][: n - 1]) + grid[row][col]
                else:
                    grid[row][col] = min(min(grid[row - 1][:col]), min(grid[row - 1][col + 1:])) + grid[row][col]
        print(grid)
        return min(grid[-1][:])
