class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            tmp = ""
            for ch in word:
                tmp += chr(ord(ch) + 1)
            word += tmp
        return word[k - 1]
