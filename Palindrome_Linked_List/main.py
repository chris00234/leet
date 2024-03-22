# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []

        while head:
            li.append(head.val)
            head = head.next
        
        for i in range(len(li)//2):
            last_ind = -1 -i
            print(li[i], li[last_ind])
            if li[i] != li[last_ind]:
                return False
        return True
