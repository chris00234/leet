# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i = 1
        tmp = head
        prev_val = tmp.val
        tmp = tmp.next
        li = []

        while tmp.next:
            next_val = tmp.next.val
            curr_val = tmp.val
            if curr_val > next_val and curr_val > prev_val:
                li.append(i)
            elif curr_val < next_val and curr_val < prev_val:
                li.append(i)
            prev_val = tmp.val
            tmp = tmp.next
            i += 1
        
        if len(li) >= 2:
            mn = float('inf')
            curr = 0
            for i in range(len(li) - 1):
                curr = li[i + 1] - li[i]
                
                if mn > curr:
                    mn = curr
            return [mn, li[-1] - li[0]] 
        return [-1,-1]
        


