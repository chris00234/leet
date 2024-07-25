class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = 0,0

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "R":
                    row = r
                    col = c
                    break
        ret = 0
        iter_ = 0
        for c in range(col, -1, -1):
            if board[row][c] == "p":
                ret += 1
                break
            if board[row][c] == "B":
                break
            
        for c in range(col, len(board)):
            if board[row][c] == "p":
                ret += 1
                print("here")
                break
            if board[row][c] == "B":
                break
            
        for r in range(row, -1, -1):
            if board[r][col] == "p":
                ret += 1
                break
            if board[r][col] =="B":
                break
            
        for r in range(row, len(board)):
            if board[r][col] == "p":
                ret += 1
                break
            if board[r][col] =="B":
                break
            
        return ret
