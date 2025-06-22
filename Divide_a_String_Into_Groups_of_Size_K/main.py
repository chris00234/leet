class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        pos = 1
        tmp = ""
        for letter in s:
            if pos <= k:
                pos += 1
                tmp += letter
            elif pos > k:
                ret.append(tmp)
                pos = 2
                tmp = letter
        
        if len(tmp) < k:
            for i in range(k - len(tmp)):
                tmp += fill
        ret.append(tmp)
        return ret
