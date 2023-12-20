# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = None
        tmp = None
        while head:
            tmp = ListNode(head.val)
            if next:
                tmp.next = next
            next = tmp
            head = head.next
        return tmp