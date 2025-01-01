class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0

        
        for ch in s:
            if ch == '1':
                right += 1
        
        ret = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            ret = max(ret, left + right)
        return ret
