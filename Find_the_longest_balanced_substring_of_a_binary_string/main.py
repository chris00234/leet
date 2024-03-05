class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = 0
        ones = 0
        find = False
        max_balanced = 0
        balanced = 0
        tmp = 0
        for i in s:
            if i == '0':
                balanced = 0
                zeros += 1
                ones = 0
                tmp = zeros
                
            if i == '1':
                zeros = 0
                ones += 1
                if ones <= tmp:
                    balanced += 2
                if balanced > max_balanced:
                    max_balanced = balanced
        return max_balanced
                

