# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head1 = list1

        for i in range(a - 1):
            head1 = head1.next
        
        tmp = head1.next
        head1.next = list2

        for i in range(b - a):
            tmp = tmp.next
        con = tmp.next

        while list2.next != None:
            list2 = list2.next
        
        list2.next = con

        return list1