class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for i in range(low, high + 1, 1):
            if len(str(i)) % 2 == 1:
                continue
            if self.isSame(i):
                ret += 1
        return ret
    def isSame(self, i):
        s = str(i)
        half = len(s) // 2
        first = s[:half]
        last = s[half:]
        f_ret = 0
        l_ret = 0
        for tmp in first:
            f_ret += int(tmp)
        for t in last:
            l_ret += int(t)
        return f_ret == l_ret
