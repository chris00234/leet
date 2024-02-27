class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {x: None for x in s}
        for i in range(len(s)):
            if dict[s[i]] == None:
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]
            else:
                if dict[s[i]] != t[i]:
                    return False

        return True
        