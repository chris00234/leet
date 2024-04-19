class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        s = set()
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if (i not in range(r) or j not in range(c) or (i, j) in s or grid[i][j] == '0'):
                return 
            s.add((i, j))
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in direction:
                dfs(i + dr, j + dc)
        
        for row in range(r):
            for col in range(c):
                if grid[row][col] == "1" and (row, col) not in s:
                    island += 1
                    dfs(row, col)

        return island
            
            


