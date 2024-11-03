class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        original = s

        tmp = s[1:] + s[0]

        while original != tmp:
            if goal == tmp:
                return True
            tmp = tmp[1:]+tmp[0]
        return False
