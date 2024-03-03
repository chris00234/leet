# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        store = []

        while node:
            store.append(node)
            node = node.next
        
        if len(store) == 1:
            head = None
            return head

        traverse = len(store) - (n + 1)
        print(traverse)
        if traverse < 0:
            head = head.next
            return head
        curr = head

        for i in range(traverse):
            curr = curr.next
        print(curr)
        if curr.next == None:
            return head
        else:
            curr.next = (curr.next).next
        
        return head