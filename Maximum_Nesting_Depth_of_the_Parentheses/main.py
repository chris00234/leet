class Solution:
    def maxDepth(self, s: str) -> int:
        num_open = 0
        max_paran = 0
        paran = 0

        for letter in s:
            if letter == "(":
                num_open += 1
            if letter == ")":
                paran = num_open
                num_open -= 1
                if max_paran < paran:
                    max_paran = paran
        
        return max_paran
            
