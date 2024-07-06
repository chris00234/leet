class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num *= 10
            num += digits[i]
        num += 1
        ret = []
        while num != 0:
            val = num % 10
            num = num // 10
            ret.append(val)
        print(ret)
        return list(reversed(ret))
