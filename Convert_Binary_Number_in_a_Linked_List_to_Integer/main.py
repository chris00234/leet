# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        ret = 0
        power = 0
        for i in range(len(values) - 1, -1, -1):
            tmp = 2**power * values[i]
            power += 1
            ret += tmp
        return ret
