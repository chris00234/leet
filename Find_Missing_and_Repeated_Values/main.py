class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n **= 2
        dic = {i: 0 for i in range(1, n + 1)}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                dic[grid[r][c]] += 1
        ret = []
        for key in dic:
            if dic[key] == 2:
                ret.append(key)
        for key in dic:
            if dic[key] == 0:
                ret.append(key)
        return ret
