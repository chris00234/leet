# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        index = math.floor(count/2)
        tmp = head
        if count == 1:
            return None

        i = 0
        while i < index - 1:
            tmp = tmp.next
            i += 1
        tmp.next = tmp.next.next
        return head
        
