class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(16, -1, -1):
            if math.pow(3, i) <= n:
                n -= math.pow(3, i)
            if n == 0:
                return True
            
        return False

