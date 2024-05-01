class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        r = 0
        for c in word:
            if c == ch:
                break
            r += 1
        if r == len(word):
            return word
        ans = ""
        for index in range(r, -1, -1):
            ans += word[index]
        
        ans += word[r + 1:]
        return ans
