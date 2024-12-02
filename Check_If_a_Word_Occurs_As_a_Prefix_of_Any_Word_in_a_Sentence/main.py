class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ret = -1

        li = sentence.split(" ")

        for idx, word in enumerate(li):
            if word.startswith(searchWord):
                return idx + 1
        return ret 
