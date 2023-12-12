# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        tmp = prev
        ans = None
        while l1 != None or l2 != None:
            if l1 == None:
                tmp = l2
                l2 = l2.next
            elif l2 == None:
                tmp = l1
                l1 = l1.next
            elif l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            if ans == None:
                ans = tmp
            prev.next = tmp
            prev = tmp
        return ans