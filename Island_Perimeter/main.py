class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def find_water_neighbor(grid, row, col):
            ret = 0
            if row == 0:
                ret += 1
            if col == 0:
                ret += 1
            if row == len(grid) - 1:
                ret += 1
            if col == len(grid[0]) - 1:
                ret += 1
            if row > 0:
                if grid[row - 1][col] == 0:
                    ret += 1
            if row < len(grid) - 1:
                if grid[row + 1][col] == 0:
                    ret += 1
            if col > 0:
                if grid[row][col - 1] == 0:
                    ret += 1
            if col < len(grid[0]) - 1:
                if grid[row][col + 1] == 0:
                    ret += 1
            return ret
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ans += find_water_neighbor(grid, row, col)
        return ans

