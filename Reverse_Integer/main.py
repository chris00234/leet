class Solution:
    def reverse(self, x: int) -> int:
        isNeg = True if x < 0 else False
        x = abs(x)
        ret = 0

        while x > 0:
            md = x % 10
            x //= 10
            ret *= 10
            ret += md
        if -2**31 > ret or ret > 2**31 -1:
            return 0
        return ret if isNeg == False else ret * -1
        
