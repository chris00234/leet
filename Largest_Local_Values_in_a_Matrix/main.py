class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ret = [[0 for i in range(n - 2)] for j in range(n - 2)]
        
        for row in range(len(ret)):
            for col in range(len(ret)):
                grid_row1 = grid[row]
                grid_row1 = max(grid_row1[col:3+col])
                grid_row2 = grid[row + 1]
                grid_row2 = max(grid_row2[col:3+col])
                grid_row3 = grid[row + 2]
                grid_row3 = max(grid_row3[col:3+col])
                max_grid_row = max(grid_row1, grid_row2, grid_row3)
                ret[row][col] = max_grid_row


        return ret

