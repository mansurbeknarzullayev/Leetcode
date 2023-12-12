# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = None
        tmp = head
        sz = 0
        while tmp:
            tmp = tmp.next
            sz += 1
        k = 0
        n = sz - n
        while head:
            if k != n:
                tmp = ListNode(head.val)
                if ans == None:
                    ans = tmp
                else:
                    last.next = tmp
                last = tmp
            head = head.next
            k += 1
        return ans