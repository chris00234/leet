class Solution:
    def minChanges(self, s: str) -> int:
        ret = 0
        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                ret += 1
        return ret
 
