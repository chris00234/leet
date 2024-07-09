class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        l = num // 3 - 1
        r = l + 2
        sm = l + l + 1 + r

        while sm <= num:
            if sm == num:
                return [l, l + 1, r]
            sm -= l
            l += 1
            r += 1
            sm += r
        return []


            
