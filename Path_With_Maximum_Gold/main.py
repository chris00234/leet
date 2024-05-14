class Solution:
    def __init__(self):
        self.roww = [1,-1, 0,0]
        self.coll = [0,0,-1,1]
    
    def backtrack(self, grid, vis, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >=m or grid[x][y] == 0 or vis[x][y]:
            return 0
        
        vis[x][y] = 1
        maxGold = grid[x][y]

        for i in range(4):
            newX = x + self.roww[i]
            newY = y + self.coll[i]
            maxGold = max(maxGold, grid[x][y] + self.backtrack(grid, vis, newX, newY, n, m))
        vis[x][y] = 0
        return maxGold
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        maxGold = 0
        vis = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.backtrack(grid, vis, i, j, n, m))
        
        return maxGold

