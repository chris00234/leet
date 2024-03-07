class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        row, col = 0,0
        output = ""
        board_map = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                board_map[board[i][j]] = i
    
        for letter in target:
            print(output)
            tmp_row = board_map[letter]
            #going down 
            if tmp_row > row:
                while row < tmp_row:
                    if row == 4:
                        break
                    row += 1
                    output += "D"
                    
                if letter == 'z':
                    while col != 0:
                        col -= 1
                        output += "L"
                    row += 1
                    output += "D"
                while board[row][col] != letter:
                    if board[row][col] < letter:
                        col += 1
                        output += "R"
                    elif board[row][col] > letter:
                        col -= 1
                        output += "L"
                    
                output += "!"

            #going up
            elif tmp_row < row:
                while row != tmp_row:
                    output += "U"
                    row -= 1
                if letter == 'z':
                    while col != 0:
                        col -= 1
                        output += "L"
                while board[row][col] != letter:
                    if board[row][col] < letter:
                        col += 1
                        output += "R"
                    elif board[row][col] > letter:
                        col -= 1
                        output += "L"
                output += "!"
            #on the same row
            else:
                if letter == 'z':
                    while col != 0:
                        col -= 1
                        output += "L"
                while board[row][col] != letter:
                    if board[row][col] < letter:
                        col += 1
                        output += "R"
                    elif board[row][col] > letter:
                        col -= 1
                        output += "L"
                output += "!"
        return output



           
            