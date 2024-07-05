class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        length = n1 if n1 < n2 else n2
        ret = ""
        i = 0
        for i in range(length):
            ret += word1[i]
            ret += word2[i]
        if length == n1:
            ret += word2[i + 1 :]
        elif length == n2:
            ret += word1[i + 1 :]
        return ret

