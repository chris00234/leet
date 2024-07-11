class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        new_str = s
        for i in range(len(s)):
            if new_str[i] == ")":
                j = i
                for j in range(i, -1, -1):
                    if new_str[j] == "(":
                        break
                
                part = new_str[j + 1: i][::-1]
                new_str = new_str[:j] + "_" + part + "_" + new_str[i + 1:]
        ret = ""
        for char in new_str:
            if char != "_":
                ret += char
        return ret
        
        
