class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        prev = ''
        ret = []
        for ch in s:
            if prev == ch:
                count += 1
            else: count = 1
            if count < 3:
                ret.append(ch)
            prev = ch
        return ''.join(ret)
