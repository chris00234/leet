class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        ch = ''
        while l < r:
            ch = s[l]
            if s[r] != s[l]:
                return r-l + 1
            else:
                if l + 1 < r:
                    if s[l + 1] == ch:
                        l = l + 1
                        continue
                if l < r - 1:
                    if s[r - 1] == ch:
                        r -= 1
                        continue
                l += 1
                r -= 1
        return r-l + 1