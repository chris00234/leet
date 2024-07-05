class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False
        while n > 0:
            for i in range(pos, len(flowerbed)):
                if i == 0:
                    if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                if n == 0:
                     break
                pos += 1
            if pos == len(flowerbed):
                break
        
        return True if n == 0 else False 
