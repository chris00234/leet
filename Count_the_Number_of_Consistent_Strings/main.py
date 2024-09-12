class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        ret = 0
        for word in words:
            if set(word).issubset(allowedSet):
                ret += 1
        return ret

            

