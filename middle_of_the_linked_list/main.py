# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next
        cnt = cnt // 2

        for i in range(cnt):
            head = head.next
        
        return head