class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        li = []
        for i in s:
            li.append(i)
        
        for i in t:
            if i in li:
                li.remove(i)
        
        if len(li) == 0:
            return True
        return False