class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s,2)
        print(num)
        ret = 0
        while num != 1:
            if num %2 == 1:
                num += 1
            else:
                num //= 2
            ret += 1
        return ret
