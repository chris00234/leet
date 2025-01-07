class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []

        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j and words[i] not in ret:
                    ret.append(words[i])
        return ret

