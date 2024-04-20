class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        res = []

        def expand_from(i, j):
            # expand a rectangle of farmland starting from (i, j) as much as possible
            bottom, right = i, j
            while bottom + 1 < rows and land[bottom + 1][j] == 1:
                bottom += 1
            while right + 1 < cols and all(land[k][right + 1] == 1 for k in range(i, bottom + 1)):
                right += 1
            
            # mark farmland as visited
            for x in range(i, bottom + 1):
                for y in range(j, right + 1):
                    land[x][y] = 0  

            res.append([i, j, bottom, right])

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:  
                    expand_from(i, j)

        return res
