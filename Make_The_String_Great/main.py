class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        pos = 0
        while pos < n - 1:
            if s[pos].lower() == s[pos + 1].lower():
                if s[pos] == s[pos + 1]:
                    pos += 1
                else:
                    s = s[:pos] + s[pos + 2:]
                    print(s)
                    pos = 0
                    n = len(s)
            else:
                pos += 1
        return s

            
