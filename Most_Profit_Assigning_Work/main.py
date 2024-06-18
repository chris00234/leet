class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit_for_difficulty = []
        infos = list(zip(difficulty, profit))
        infos.sort(key = lambda x: x[0])
        maxp = 0
        for info in infos:
            d, p = info
            maxp = max(maxp, p)
            max_profit_for_difficulty.append((d,maxp))
        
        def binsearch(L, upperbound):
            i = 0 
            j = len(L) - 1
            while i<j:
                mid = (i+j)//2 + 1
                if L[mid][0] <= upperbound:
                    i = mid
                else:
                    j = mid - 1
            return i
        
        totalprof = 0
        for w in worker:
            ind = binsearch(max_profit_for_difficulty, w)
            d, p = max_profit_for_difficulty[ind]
            if w >= d:
                totalprof += p
        return totalprof


