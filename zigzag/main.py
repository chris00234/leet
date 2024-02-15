class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mat = [[] for i in range(numRows)]
        
        row = 0
        col = 0
        pullDown = True
        if numRows == 1:
            return s
        for char in s:
            if row == 0:
                pullDown = True
            if row == numRows - 1:
                pullDown = False
            if pullDown == True:
                mat[row].append(char)
                row += 1
            else:
                mat[row].append(char)
                row -= 1
        
        ans = ""
        for r in range(numRows):
            for c in mat[r]:
                ans += c
        return ans
            