class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
        
        result = ""
        ones -= 1
        for i in range(length - 1):
            if ones > 0:
                result += '1'
                ones -= 1
            else:
                result += '0'
        
        result += '1'
        return result