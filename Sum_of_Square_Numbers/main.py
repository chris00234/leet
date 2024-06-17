class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num = math.sqrt(c)
        max_num = math.floor(max_num)
        arr = [i for i in range(max_num + 1)]
        print(arr)
        # if len(arr) <= 1:
        #     return False
        
        l = 0
        r = arr[-1]
        while l <= r:
            if l ** 2 + r **2 == c:
                return True
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                r -= 1
        return False

