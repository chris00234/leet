class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        rev = False
        t = 0
        while t < time:
            if i == n:
                rev = True
            if i == 1:
                rev = False
            if rev == False:
                i += 1
            else:
                i -= 1
            t += 1
        return i
            
