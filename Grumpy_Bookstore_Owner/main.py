class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        mx = 0
        gr_pos = 0
        ret = 0
        for i in range(len(customers) - minutes + 1):
            curr = 0
        
            for k in range(i, i + minutes):
                if grumpy[k] == 1:
                    curr += customers[k]
            # print(f'pos = {i} and curr = {curr} where customers[i] = {customers[i]}')
                
            if curr > mx:
                mx = curr
                gr_pos = i
 
        for j in range(gr_pos, gr_pos + minutes):
            grumpy[j] = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                ret += customers[i]
        return ret

