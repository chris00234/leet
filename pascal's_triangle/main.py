class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = {}
        triangle[0] = [1]
        triangle[1] = [1,1]

        for i in range(2, numRows):
            li = [1 for j in range(i + 1)]
            pos = 1
            for k in range(len(triangle[i - 1])):
                if k + 1 < len(triangle[i -1]):
                    li[pos] = triangle[i-1][k] + triangle[i-1][k+1]
                pos += 1
            triangle[i] = li
        
        if numRows == 1:
            return [[1]]
        return list(triangle.values())
