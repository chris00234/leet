class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        min = 0
        for i in range(1, k + 1):
            min += i
        
        if n < min:
            return []
        
        def backtrack(li, total, start):
            if len(li) == k:
                if total == n:
                    res.append(li.copy())
                    print(res)
                return
            
            for i in range(start, 10):
                li.append(i)
                backtrack(li, total + i, i + 1)
                li.pop()
        
        res = []
        backtrack([], 0, 1)
        return res
