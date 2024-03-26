class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = [0 for i in range(n + 1)]
    
        # memo[0] = 1
        # memo[1] = 1
        

        # for i in range(2, n + 1):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        
        # return memo[n]

        if n <= 2:
            return n

        memo = {}
        def recur(n):
            if n < 2:
                return 1
            
            if n not in memo:
                memo[n] = recur(n - 1) + recur(n - 2)
            return memo[n]

        return recur(n)




        

        
