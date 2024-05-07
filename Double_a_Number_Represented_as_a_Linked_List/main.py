# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        while head:
            num *= 10
            num += head.val
            head = head.next
        num *= 2
        stack = []
        while num:
            stack.append(num%10)
            num = num // 10
    
        ans = ListNode()
        tmp = ans
        pos = 0
        n = len(stack)
       
        while stack:
            tmp.val = stack.pop()
            print(tmp.val)
            
            if pos < n - 1:
                tmp.next = ListNode()
                tmp = tmp.next
            pos += 1
        
        return ans


