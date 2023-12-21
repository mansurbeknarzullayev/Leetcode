# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        tmp = head
        sz = 0
        while tmp:
            tmp = tmp.next
            sz += 1
        sz //= 2
        last = None
        cnt = 0
        while head:
            tt = ListNode(head.val)
            if cnt != sz:
                if ret == None:
                    ret = tt
                else:
                    last.next = tt
                last = tt
            cnt += 1
            head = head.next
        return ret