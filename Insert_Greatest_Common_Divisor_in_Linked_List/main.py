# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head

        while tmp.next:
            cval = tmp.val
            nval = tmp.next.val
            g = gcd(cval, nval)
            node = ListNode(g, tmp.next)
            tmp.next = node
            tmp = node.next
        return head
