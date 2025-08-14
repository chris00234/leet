class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ret = ""
        for i in range(len(num) - 2):
            digit_list = list(num[i:i + 3])
            if len(set(digit_list)) == 1:
                if ret == "":
                    ret = num[i:i + 3]
                else:
                    if int(ret) < int(num[i:i+3]):
                        ret = num[i:i+3]
        return ret
            
