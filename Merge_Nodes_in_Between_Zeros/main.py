# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        s = 0
        li = []

        while tmp:
            if tmp.val == 0:
                li.append(s)
                s = 0
            else:
                s += tmp.val
            tmp = tmp.next
        tmp = ListNode(li[1])
        head = tmp
        for i in range(2, len(li)):
            tmp.next = ListNode(li[i])
            tmp = tmp.next
        return head
