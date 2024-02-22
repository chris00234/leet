class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        store_zeros = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    store_zeros.append((row, col))
        
        for i in range(len(store_zeros)):
            for c in range(len(matrix[0])):
                matrix[store_zeros[i][0]][c] = 0
            for r in range(len(matrix)):
                matrix[r][store_zeros[i][1]] = 0
                    
                        

                    
        