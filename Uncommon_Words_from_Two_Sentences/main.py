

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2

        li = s.split(" ")

        mp = {}
        for word in li:
            mp[word] = mp.get(word, 0) + 1
        
        ret = []
        for word in mp:
            if mp[word] == 1:
                ret.append(word)

        return ret
