class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def live_neighbors(board, r, c) -> int:
            result = 0
            if r - 1 >= 0:
                if c - 1 >= 0:
                    if board[r - 1][c - 1] == 1:
                        result += 1
                if c + 1 < len(board[0]):
                    if board[r - 1][c + 1] == 1:
                        result += 1
                if board[r - 1][c] == 1:
                    result += 1
            if r + 1 < len(board):
                if c - 1 >= 0:
                    if board[r + 1][c - 1] == 1:
                        result += 1
                if c + 1 < len(board[0]):
                    if board[r + 1][c + 1] == 1:
                        result += 1
                if board[r + 1][c] == 1:
                    result += 1
            if c - 1 >= 0:
                if board[r][c- 1] == 1:
                    result += 1
            if c + 1 < len(board[0]):
                if board[r][c+1] == 1:
                    result += 1
            return result
        
        output = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 1:
                    n = live_neighbors(board, r, c)
                    if n < 2:
                        output[r][c] = 0
                    elif 2 <= n<= 3:
                        output[r][c] = 1
                    else:
                        output[r][c] = 0
                else:
                    n = live_neighbors(board, r, c)
                    if n == 3:
                        output[r][c] = 1 

        import copy
        print(output)
        for r in range(len(output)):
            for c in range(len(output[0])):
                board[r][c] = output[r][c]
      
        
