class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ret = 0
        for i in range(len(words) - 1):
            for j in range(len(words) - 1, i, -1):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ret += 1
        return ret
