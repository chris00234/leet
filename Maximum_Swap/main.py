class Solution:
    def maximumSwap(self, num: int) -> int:
        li = []
        while num > 0:
            mod = num % 10
            li.append(mod)
            num //=10
        
        li.reverse()
        for i in range(len(li) - 1):
            ind = 0
            mx = max(li[i:])
            if li[i] != mx:
                for j in range(i + 1, len(li)):
                    if li[j] == mx:
                        ind = j
                li[i], li[ind] = li[ind], li[i]
                break
        ret = 0
        for el in li:
            ret *= 10
            ret += el
            
        
        return ret

