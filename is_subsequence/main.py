class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = ""
        j = 0
        if s == "":
            return True
        for i in range(len(t)):
            if j >= len(s):
                break
            if t[i] == s[j]:
                result += s[j]
                j += 1
        
        if result == s:
            return True
        return False