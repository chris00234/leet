class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        ret = 0

        for i in range(r):
            tmp = 0
            visited = []
            for j in range(c):
                if grid[i][j] == 1:
                    tmp += 1
                    visited.append([i,j])
            if tmp > 1:
                ret += tmp
                for visit in visited:
                    grid[visit[0]][visit[1]] = -1
            

        
        for i in range(c):
            tmp = 0
            actual = 0
            for j in range(r):
                if grid[j][i] == 1 or grid[j][i] == -1:
                    tmp += 1
                if grid[j][i] == 1:
                    actual += 1
            if tmp > 1:
                ret += actual
        return ret
            
