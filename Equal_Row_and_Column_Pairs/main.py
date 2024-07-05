class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        dict_r = []
        for r in range(len(grid)):
            tmp = []
            for c in range(len(grid[0])):
                tmp.append(grid[r][c])
            dict_r.append(tmp)
        
        dict_c = []
        for c in range(len(grid[0])):
            tmp = []
            for r in range(len(grid)):
                tmp.append(grid[r][c])
            dict_c.append(tmp)
        
        for key_r in dict_r:
            for key_c in dict_c:
                if key_r == key_c:
                    ret += 1
        return ret

