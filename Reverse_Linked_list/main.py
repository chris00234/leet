# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            stack.append(head)
            head = head.next

        res =ListNode()
        ans = res
        while len(stack) != 0:
            tmp = ListNode(val = stack.pop().val)
            res.next = tmp
            res = res.next
        return ans.next
