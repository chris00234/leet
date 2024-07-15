class Solution:
    def myAtoi(self, s: str) -> int:
        isNum = False
        isNeg = False
        isSign = False
        ret = 0
        for char in s:
            if char == " " and not isNum and not isSign:
                continue
            elif (char == "-" or char == "+") and not isNum:
                if isSign == True:
                    break
                if char == "-":
                    isNeg = True
                isSign = True
            elif ord(char) - ord("0") >= 0 and ord(char) - ord("0") <= 9:
                isNum = True
                ret *= 10
                ret += ord(char) - ord("0")
            else:
                break
        ret = ret if isNeg == False else ret * -1
        if ret < -2**31:
            return -2**31
        elif ret > 2**31 - 1:
            return 2**31 -1
        return ret
                
                
