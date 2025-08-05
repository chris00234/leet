class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ret = len(fruits)

        for fruit in fruits:
            idx = 0
            pop = False
            for idx in range(len(baskets)):
                print(baskets[idx])
                if baskets[idx] >= fruit:
                    ret -= 1
                    pop = True
                    break
            if pop:
                baskets.pop(idx)
        return ret
            

