class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        mp = {}
        if len(set(s)) != len(set(t)):
            return False
        
        for i in range(n):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                mp[s[i]] = t[i]

        
        return True
        