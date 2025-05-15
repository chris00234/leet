class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i = 0
        prev = -1
        ret = []
        for i in range(len(groups)):
            if prev != groups[i]:
                ret.append(words[i])
                prev = groups[i]
        return ret
