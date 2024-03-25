# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li = []

        node = head

        while node:
            if len(li) < n:
                print(node)
                li.append(node)
            elif len(li) == n:
                li.pop(0)
                li.append(node)
                
            node = node.next
        
        res = head
        prev = None
        print(li)
        while res:
            if res == li[0]:
                if prev == None:
                    head = res.next
                    break
                prev.next = res.next
                break
            prev = res
            res = res.next

        
        return head
