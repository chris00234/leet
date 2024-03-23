# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        curr = head

        while curr:
            place_holder = curr
            last = curr
            last_prev = curr
            while place_holder.next:
                last_prev = place_holder
                last = place_holder.next
                place_holder = place_holder.next
            last_prev.next = None
            curr_next = curr.next
            curr.next = last
            last.next = curr_next
            curr = curr_next

            


        