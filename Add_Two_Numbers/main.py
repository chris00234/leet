# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        val2 = 0

        ind = 1
        while l1:
            val1 += l1.val * ind
            ind *= 10
            l1 = l1.next
        ind = 1
        while l2:
            val2 += l2.val * ind
            ind *= 10
            l2 = l2.next
        
        ans = val1 + val2
        print(ans)
        l3 = ListNode(0)
        ret = l3

      

        while ans:
            newNode = ListNode(ans%10)
            l3.next = newNode
            l3 = l3.next
            ans = ans//10
        
        if ret.next:
            return ret.next
        else:
            return ret
