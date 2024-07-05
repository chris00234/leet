class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        elif len(t) == len(s) and s != t:
            return False
        pos = 0
        for i in range(len(s)):
            for j in range(pos, len(t)):
                pos += 1
                if s[i] == t[j]:
                    break
                if j == len(t) - 1 and s[i] != t[j]:
                    return False
            if pos == len(t) and i < len(s) - 1:
                return False
                
        return True

