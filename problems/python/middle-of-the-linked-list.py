# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        last = head
        while last:
            last = last.next
            if last:
                last = last.next
                ans = ans.next
        return ans