class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rowMin = float('inf')
        rowMax = -1
        colMin = float('inf')
        colMax = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rowMin = min(rowMin, i)
                    colMin = min(colMin, j)
                    rowMax = max(rowMax, i)
                    colMax = max(colMax, j)
        return (rowMax - rowMin + 1) * (colMax - colMin + 1)
                    
