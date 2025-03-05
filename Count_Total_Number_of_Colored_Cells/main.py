class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 5
        n = 2* (n - 1) + 1
        ret = n
        while n > 1:
            n -= 2
            ret += (n * 2)
        return ret

