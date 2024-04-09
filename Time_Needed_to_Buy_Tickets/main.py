class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        second = 0
        n = len(tickets)
        while len(tickets) != 0:
            tickets[0] -= 1
            if tickets[k] == 0:
                break
            if tickets[0] != 0:
                tickets.append(tickets.pop(0))
            else:
                tickets.pop(0)
            if k == 0:
                k = len(tickets) - 1
            else:
                k -= 1
            second += 1
            
        return second + 1
            
