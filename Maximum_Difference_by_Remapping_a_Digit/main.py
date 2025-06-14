class Solution:
    def minMaxDifference(self, num: int) -> int:
        mx = 0
        mn = float('inf')

        numStr = str(num)
        numLi = list(numStr)
        tmp = ''
        for i in range(len(numLi)):
            if numLi[i] != '9' and tmp == '':
                tmp = numLi[i]
                numLi[i] = '9'
            elif numLi[i] == tmp:
                numLi[i] = '9'
        mx = int("".join(numLi))

        numLi = list(numStr)
        tmp = ''
        for i in range(len(numLi)):
            if numLi[i] != '0' and tmp == '':
                tmp = numLi[i]
                numLi[i] = '0'
            elif numLi[i] == tmp:
                numLi[i] = '0'
        mn = int("".join(numLi))

        return mx - mn



