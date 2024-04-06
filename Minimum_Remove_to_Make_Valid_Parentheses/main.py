class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        val = 0
        for letter in s:
            if letter == '(':
                stack.append(letter)
            elif letter == ')' and len(stack) != 0:
                stack.pop()
                val += 1
        
        ans = ""
        num_opened = 0
        for letter in s:
            if letter == '(' and val > num_opened:
                num_opened += 1
                ans += letter
            elif letter == ')' and val >0 and num_opened > 0:
                val -= 1
                num_opened -= 1
                ans += letter
            elif letter != '(' and letter != ')':
                ans += letter
        
        return ans
        
        
