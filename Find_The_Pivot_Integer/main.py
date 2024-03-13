class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = 0
        postfix_sum = 0
        for j in range(1, n+ 1):
            postfix_sum += j
        for i in range(1, n + 1):
            prefix_sum += i
            if prefix_sum == postfix_sum:
                return i
            else:
                postfix_sum -= i
        
        return -1
